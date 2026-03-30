import os
import pandas as pd
from dotenv import load_dotenv

# Load Environment Telemetry (Treasury Yield: 4.44%, Oil: $104.15)
load_dotenv()

def run_telemetry():
    # Macro Constants from .env
    us10y = float(os.getenv("TREASURY_YIELD_10Y", 4.44))
    oil_price = float(os.getenv("CRUDE_OIL_PRICE", 100.0))
    infra_mult = float(os.getenv("INFRA_MULTIPLIER", 1.5))
    promo_mult = float(os.getenv("INDEX_PROMO_MULTIPLIER", 1.25))

    # Core Data: Mapped from Mar 23 Rebalance & Mar 30 Bloomberg Close
    data = {
        "ticker": ["NVDA", "MSFT", "MU", "VRT", "LITE", "XOM", "PETR4", "PYPL", "MTCH"],
        "roic": [32.5, 21.5, 28.4, 18.2, 12.4, 14.1, 15.2, 9.1, 10.5],
        "wacc": [10.2, 9.8, 9.5, 8.5, 9.1, 7.2, 11.2, 11.5, 8.2],
        "is_infra": [True, True, True, True, True, False, False, False, False],
        "index_event": ["MAINTAIN", "MAINTAIN", "S100_PROMO", "S500_ADD", "S500_ADD", "MAINTAIN", "TACTICAL", "S100_DEL", "S500_DEL"]
    }

    df = pd.DataFrame(data)
    
    # 1. Calculate EVA Spread (ROIC - WACC)
    df['spread'] = df['roic'] - df['wacc']
    
    # 2. Apply Yield-Adjusted Discounting (Discounting for 4.44% Yield)
    yield_penalty = us10y / 10.0
    df['alpha'] = df['spread'] - yield_penalty
    
    # 3. Apply Strategic Multipliers for AI Sovereignty and Index Momentum
    df.loc[df['is_infra'], 'alpha'] *= infra_mult
    df.loc[df['index_event'].str.contains("ADD|PROMO"), 'alpha'] *= promo_mult

    # 4. Signal Generation Logic for the April 6 Window
    def get_signal(row):
        if "DEL" in row['index_event'] or row['alpha'] < 0:
            return "EXIT (PASSIVE SELLING)"
        if row['alpha'] > 18.0:
            return "CORE (SOVEREIGN ANCHOR)"
        if row['ticker'] in ["XOM", "PETR4"] and oil_price > 100:
            return "HEDGE (STAGFLATION)"
        return "ACCUMULATE"

    df['signal'] = df.apply(get_signal, axis=1)

    # Display Output
    print(f"\n" + "="*60)
    print(f"STARGATE TELEMETRY | MAR 30, 2026 | OIL: ${oil_price} | 10Y: {us10y}%")
    print(f"="*60)
    print(df[['ticker', 'spread', 'alpha', 'signal']].sort_values(by='alpha', ascending=False).to_string(index=False))
    print(f"="*60 + "\n")

if __name__ == "__main__":
    run_telemetry()
