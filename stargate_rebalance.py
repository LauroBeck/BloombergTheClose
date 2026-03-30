import os
import pandas as pd
from dotenv import load_dotenv

# Load Environment Telemetry (Treasury Yield: 4.44% | Oil: $104.15)
load_dotenv()

def run_telemetry():
    # Macro Constants from .env
    us10y = float(os.getenv("TREASURY_YIELD_10Y", 4.44))
    oil_price = float(os.getenv("CRUDE_OIL_PRICE", 104.15))
    infra_mult = float(os.getenv("INFRA_MULTIPLIER", 1.5))
    
    # Core Data: Mar 30 Close (IBM: $237.25 | S&P: -0.39%)
    data = {
        "ticker": ["NVDA", "MU", "IBM", "VRT", "MSFT", "XOM", "PETR4", "PYPL", "MTCH"],
        "roic": [32.5, 28.4, 13.75, 18.2, 21.5, 14.1, 15.2, 9.1, 10.5],
        "wacc": [10.2, 9.5, 10.10, 8.5, 9.8, 7.2, 11.2, 11.5, 8.2],
        "is_infra": [True, True, True, True, True, False, False, False, False],
        "index_event": ["MAINTAIN", "S100_PROMO", "MAINTAIN", "S500_ADD", "MAINTAIN", "MAINTAIN", "TACTICAL", "S100_DEL", "S500_DEL"]
    }

    df = pd.DataFrame(data)
    
    # 1. Calculate EVA Spread
    df['spread'] = df['roic'] - df['wacc']
    
    # 2. Yield-Adjusted Alpha (4.44% Yield Penalty)
    yield_penalty = us10y / 10.0
    df['alpha'] = df['spread'] - yield_penalty
    
    # 3. Apply Sovereign Multipliers (IBM classified as Critical AI Infra)
    df.loc[df['is_infra'], 'alpha'] *= infra_mult

    # 4. Signal Generation Logic
    def get_signal(row):
        if "DEL" in row['index_event'] or row['alpha'] < 0:
            return "EXIT (PASSIVE SELLING)"
        if row['alpha'] > 18.0:
            return "CORE (SOVEREIGN ANCHOR)"
        if row['ticker'] == "IBM":
            return "STRENGTH (INVERSE ANCHOR)"
        if row['ticker'] in ["XOM", "PETR4"] and oil_price > 100:
            return "HEDGE (STAGFLATION)"
        return "ACCUMULATE"

    df['signal'] = df.apply(get_signal, axis=1)

    # Sorted Output
    print(f"\nSTARGATE TELEMETRY | MAR 30, 2026 | OIL: ${oil_price} | 10Y: {us10y}%")
    print("="*65)
    print(df[['ticker', 'spread', 'alpha', 'signal']].sort_values(by='alpha', ascending=False).to_string(index=False))
    print("="*65 + "\n")

if __name__ == "__main__":
    run_telemetry()
