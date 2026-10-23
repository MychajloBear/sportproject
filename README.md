# Sports Course Bookings - Raw Data Generator 🚴‍♂️⚽

A lightweight, dependency-free Python script that generates simulated raw booking data for sports courses at a fictional club (**Eintracht Fliegenhausen e.V.**) and exports it to a CSV file.

## Features

- **Standard Library Only:** Built using only Python's built-in modules (`csv`, `random`, `datetime`). **No external libraries (like Pandas) are required.**
- **Reproducible Data:** Uses a fixed random seed (`random.seed(42)`) to ensure the exact same dataset is generated on every run.
- **Configurable Settings:** Easily adjust the total number of bookings, age ranges, member percentages, and club offerings.
- **Clean Structure:** Written following Python best practices, including modular functions, descriptive docstrings, and a standard `main()` entry point.

---

## Output CSV Structure

The script generates a semicolon-delimited (`;`) CSV file (`bookings_raw_data.csv`) containing the following columns:

| Column | Description | Example |
| :--- | :--- | :--- |
| **Date** | ISO format date of the booking | `2026-03-14` |
| **BookingID** | Unique sequential booking identifier | `B0001` |
| **Sport** | Name of the sport discipline | `Badminton` |
| **Age** | Age of the participant (6–15) | `12` |
| **UnitPrice** | Regular price of the course in Euros | `90` |
| **TotalPrice** | Final price after member discounts | `50` |
| **Discount** | Member discount applied (if applicable) | `40` |
| **MemberNo** | Member identifier (empty for non-members) | `M1042` |

---

## Prerequisites

- **Python 3.x** installed on your system.

---

## Usage

1. Clone the repository or download the script file.
2. Run the script directly from your terminal:

```bash
python generator.py
