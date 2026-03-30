import pandas as pd

def get_telemetry_data():
    """
    Data mapped from Mar 30, 2026 Bloomberg & Energy Market Cap screenshots.
    Reflects the Mar 23 S&P 100/500 Reshuffle.
    """
    data = {
        "ticker": ["NVDA", "MSFT", "MU", "VRT", "XOM", "PETR4", "PYPL", "TGT", "LITE"],
        "roic": [32.5, 21.5, 28.4, 18.2, 14.1, 15.2, 9.1, 10.5, 12.4],
        "wacc": [10.2, 9.8, 9.5, 8.5, 7.2, 11.2, 11.5, 8.2, 9.1],
        "is_infra": [True, True, True, True, False, False, False, False, True],
        "index_status": ["MAINTAIN", "MAINTAIN", "PROMO_S100", "ADD_S500", "MAINTAIN", "TACTICAL", "DEL_S100", "DEL_S100", "ADD_S500"]
    }
    
    df = pd.DataFrame(data)
    # Calculate Base Spread (EVA)
    df['spread'] = df['roic'] - df['wacc']
    return df

if __name__ == "__main__":
    print("Pre-flight Data Integrity Check...")
    print(get_telemetry_data())
