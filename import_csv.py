"""
Raw Data Generator: Sports Course Bookings (one participant per booking)
Club: Eintracht Fliegenhausen e.V. (simulated data)

Uses standard library only (csv, random, datetime).
"""

import csv
import os
import random
from datetime import date, timedelta

# Settings
TOTAL_BOOKINGS = 400
AGE_MIN = 6
AGE_MAX = 15
MEMBER_PERCENTAGE = 60
TOTAL_MEMBERS = 150
FILENAME = "bookings_raw_data.csv"

# Club Offerings & Helper Function
SPORTS = {}

def add_sport(name, unit_price, member_discount):
    """
    Adds a sport discipline with its pricing and member discount rules to the dictionary.

    Parameters:
    - name (str): The name of the sport discipline.
    - unit_price (int): Regular price of the course in Euros/Dollars.
    - member_discount (int): Fixed discount in Euros/Dollars applied exclusively to members.
    """
    SPORTS[name] = {"unit_price": unit_price, "member_discount": member_discount}

add_sport("Badminton", 90, 40)
add_sport("Basketball", 90, 40)
add_sport("Archery", 100, 40)
add_sport("Cheerleading", 90, 30)
add_sport("Fencing", 90, 25)
add_sport("Groupfitness", 70, 40)
add_sport("Handball", 90, 30)
add_sport("Hockey", 120, 25)
add_sport("Karate", 90, 30)
add_sport("Athletics", 80, 40)
add_sport("Padel-Tennis", 120, 30)
add_sport("Parkour", 90, 30)
add_sport("Dance", 90, 30)
add_sport("Tennis", 120, 20)
add_sport("Table-Soccer", 100, 30)
add_sport("Triathlon", 100, 20)
add_sport("Tricking", 90, 20)
add_sport("Gymnastics", 80, 30)
add_sport("Hiking", 120, 40)
add_sport("Walking", 120, 40)
add_sport("Yoga", 100, 30)

SPORT_NAMES = list(SPORTS.keys())
MEMBER_NUMBERS = [f"M{1000 + n}" for n in range(1, TOTAL_MEMBERS + 1)]
START_DATE = date(2026, 1, 1)

BOOKINGFIELDNAMES = [
    "Date",
    "BookingID",
    "Sport",
    "Age",
    "UnitPrice",
    "TotalPrice",
    "Discount",
    "MemberNo",
]

random.seed(42)

# Generate records directly and write to CSV
with open(FILENAME, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=BOOKINGFIELDNAMES, delimiter=";")
    writer.writeheader()

    for number in range(1, TOTAL_BOOKINGS + 1):
        sport = random.choice(SPORT_NAMES)
        info = SPORTS[sport]
        
        is_member = random.randint(1, 100) <= MEMBER_PERCENTAGE
        member_no = random.choice(MEMBER_NUMBERS) if is_member else ""
        discount = info["member_discount"] if is_member else 0

        booking = {
            "Date": (START_DATE + timedelta(days=random.randint(0, 272))).isoformat(),
            "BookingID": f"B{number:04d}",
            "Sport": sport,
            "Age": random.randint(AGE_MIN, AGE_MAX),
            "UnitPrice": info["unit_price"],
            "TotalPrice": info["unit_price"] - discount,
            "Discount": discount,
            "MemberNo": member_no,
        }
        
        writer.writerow(booking)

print(f"{TOTAL_BOOKINGS} bookings saved to '{FILENAME}'.")
print("Saved location:", os.path.abspath(FILENAME))