import datetime

def calculate_market_posture():
    # Mar 30 Close Data
    current_spx = 6343.72
    hard_floor = 6145.00
    recovery_target = 6500.00
    
    # Distance Calculations
    dist_to_floor = ((current_spx - hard_floor) / current_spx) * 100
    dist_to_recovery = ((recovery_target - current_spx) / current_spx) * 100
    
    print(f"\n--- STARGATE MARKET POSTURE | {datetime.date.today()} ---")
    print(f"Current Level:        {current_spx}")
    print(f"Hard Floor (6145):    {dist_to_floor:.2f}% (Support Buffer)")
    print(f"Bullish Pivot (6500): {dist_to_recovery:.2f}% (Breakout Gap)")
    print("-" * 50)
    
    if current_spx > recovery_target:
        print("SIGNAL: BULLISH RESUMPTION | REDUCE HEDGE | LONG GROWTH")
    elif current_spx < hard_floor:
        print("SIGNAL: SYSTEMIC SNAP | MAX HEDGE | EXIT GROWTH")
    else:
        print("SIGNAL: RESISTANCE ACTIVE | MAINTAIN DEFENSIVE POSTURE")
        print("FOCUS: INVERSE ANCHORS (IBM) & SCARCITY ALPHAS (CVX/XOM)")
    print("-" * 50 + "\n")

if __name__ == "__main__":
    calculate_market_posture()
