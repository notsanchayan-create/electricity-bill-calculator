# BPDB Electricity Bill Calculator
# Calculates monthly electricity bill based on power consumption and agreed limit


power_consumption = float(input("Enter power consumption (kWh): "))
agreed_limit = int(input("Enter the agreed limit (1-50):"))

if power_consumption < 0:
    print("Power cannot be negative")
    exit()

if agreed_limit < 1 or agreed_limit > 50:
    print("Agreed limit must be between 1 and 50")
    exit()

tariff_per_unit = 8.39
meter_rent = 40
fixed_charge = agreed_limit * 42 + meter_rent

energy_cost = power_consumption * tariff_per_unit
sub_total = energy_cost + fixed_charge
tax = sub_total * 0.05
grand_total = sub_total + tax

if agreed_limit <= 7:
    connection_type = "Single-Phase Connection"
else:
    connection_type = "Three-Phase Connection"

if power_consumption == 0:
    print(f"Connection type: {connection_type}")
    print(f"No power consumption, Bill (Fixed charges only) = {grand_total} TK")
else:
    print(f"Connection type: {connection_type}")
    print(f"Sub total: {sub_total} TK")
    print(f"Tax (5%): {round(tax, 2)} TK")
    print(f"Total bill: {round(grand_total, 2)} TK")

