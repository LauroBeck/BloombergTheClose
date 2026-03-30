import os
from dotenv import load_dotenv
from prepare import get_telemetry_data

# Load Telemetry Constants
load_dotenv()

def execute_stargate_protocol():
    # Macro Inputs from .env
    yield_10y = float(os.getenv("TREASURY_YIELD_10Y", 4.44))
    infra_mult = float(os.getenv("INFRA_MULTIPLIER", 1.50))
    promo_mult = float(os.getenv("INDEX_PROMO_MULTIPLIER", 1.25))
    
    df = get_telemetry_data()

    # Alpha Logic: 
    # 1. Start with ROIC Spread
    # 2. Apply Yield Penalty (Cost of Capital scaling)
    # 3. Multiply by Sovereign & Index status
    yield_penalty = yield_10y / 10.0
    df['alpha'] = df['spread'] - yield_penalty
    
    # Apply Strategic Multipliers
    df.loc[df['is_infra'], 'alpha'] *= infra_mult
    df.loc[df['index_status'].str.contains("PROMO|ADD"), 'alpha'] *= promo_mult

    # Define Signals for the April 6 Window
    def generate_signal(row):
        if row['index_status'].startswith("DEL") or row['alpha'] < 0:
            return "EXIT (PASSIVE SELLING)"
        if row['alpha'] > 18.0:
            return "CORE (SOVEREIGN ANCHOR)"
        if row['ticker'] in ["XOM", "PETR4"]:
            return "HEDGE ($100 OIL)"
        return "ACCUMULATE"

    df['signal'] = df.apply(generate_signal, axis=1)

    # Output Telemetry
    print(f"\n========================================================")
    print(f"  STARGATE TELEMETRY: MAR 30, 2026 | 10Y YIELD: {yield_10y}%")
    print(f"========================================================")
    result = df[['ticker', 'spread', 'alpha', 'signal']].sort_values(by='alpha', ascending=False)
    print(result.to_string(index=False))
    print(f"========================================================\n")

if __name__ == "__main__":
    execute_stargate_protocol()
