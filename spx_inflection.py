import os
import datetime

def calculate_snap_probability():
    # Mar 30 Close Data
    spx_now = 6343.72
    hard_floor = 6145.00
    oil_price = 115.38  
    days_to_deadline = 7 
    
    # Inflection Factors
    yield_pressure = 4.44 / 10.0
    oil_drag = (oil_price - 100) / 100
    
    # Calculate "Structural Gravity"
    gravity = (oil_drag + yield_pressure) * (1 / days_to_deadline)
    inflection_point = spx_now * (1 - (gravity * 0.1))
    
    status_header = f"\n--- S&P 500 INFLECTION ARCHITECTURE | {datetime.date.today()} ---"
    print(status_header)
    print(f"Current Level:        {spx_now}")
    print(f"Projected Inflection: {inflection_point:.2f}")
    print(f"Hard Floor:           {hard_floor}")
    print("-" * 45)
    
    if inflection_point < hard_floor:
        print("STATUS: SYSTEMIC SNAP RISK (HIGH)")
        print("ACTION: MAX HEDGE (XOM/CVX/PETR4)")
    else:
        buffer = ((inflection_point - hard_floor)/spx_now)*100
        print("STATUS: REGULATED RETRACEMENT")
        print(f"BUFFER: {buffer:.2f}% above floor.")
    print("-" * 45 + "\n")

if __name__ == "__main__":
    calculate_snap_probability()
