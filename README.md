# BPDB Electricity Bill Calculator

A Python script that calculates your monthly electricity bill based on Bangladesh Power Development Board (BPDB) tariffs.

## Features
- Calculates energy cost based on power consumption (kWh)
- Applies fixed connection charges and taxes
- Detects connection type (Single-Phase or Three-Phase)
- Validates user input

## How to Run

1. Make sure Python is installed on your system
2. Run the script:
python electricity_bill.py
3. Enter your power consumption in kWh (kilowatt-hours)
4. Enter your agreed connection limit (1-50)
5. View your bill breakdown

## Example Usage
Enter power consumption (kWh): 100

Enter the agreed limit (1-50): 7
Connection type: Single-Phase Connection

Sub total: 954.35 TK

Tax (5%): 47.72 TK

Total bill: 1002.07 TK

## Tariff Details
- Tariff rate: 8.39 TK per kWh
- Meter rent: 40 TK
- Fixed charge: (Agreed limit × 42) + 40 TK
- Tax: 5% on total

## Requirements
- Python 3.6 or higher

## Author
Created for BPDB bill calculation.
