import os

def calculate_inflection():
    current_spx = 6343.72  # From Bloomberg Terminal Mar 30
    hard_floor = 6145.00   # Technical Institutional Support
    oil_price = 104.15     # Current Risk Factor (Hormuz Blockade)
    
    # Distance to Inflection
    drop_to_floor = ((current_spx - hard_floor) / current_spx) * 100
    
    print(f"\n--- S&P 500 INFLECTION MONITOR | MAR 30, 2026 ---")
    print(f"Current Level:    {current_spx}")
    print(f"Technical Floor:  {hard_floor}")
    print(f"Distance to Floor: {drop_to_floor:.2f}%")
    print("-" * 45)
    
    if oil_price > 110:
        print("CRITICAL: High Oil is degrading the Support Floor.")
    elif drop_to_floor < 2.0:
        print("SIGNAL: Approaching Major Technical Inflection Point.")
    else:
        print("STATUS: Defensive Consolidation (Buffer Active).")
    print("-" * 45 + "\n")

if __name__ == "__main__":
    calculate_inflection()
