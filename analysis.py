import pandas as pd
import matplotlib.pyplot as plt

def generate_visual_telemetry():
    # Data extracted from Mar 30 Bloomberg Screenshot
    # IBM: +0.39% | CVX: +0.09% | SPX: -0.39% | NDX: -0.73%
    data = {
        "Asset": ["IBM", "CVX", "S&P 500", "Nasdaq 100"],
        "Performance": [0.39, 0.09, -0.39, -0.73],
        "Type": ["Infra", "Energy", "Benchmark", "Benchmark"]
    }
    
    df = pd.DataFrame(data)
    
    # Calculate Resilience Delta (Asset Performance - Nasdaq Baseline)
    ndx_baseline = -0.73
    df['Resilience_Delta'] = df['Performance'] - ndx_baseline
    
    # Plotting the "Sovereign Divergence"
    plt.figure(figsize=(10, 6))
    colors = ['green' if x > 0 else 'red' for x in df['Performance']]
    plt.bar(df['Asset'], df['Performance'], color=colors)
    
    plt.axhline(0, color='black', linewidth=0.8)
    plt.title("Bloomberg Close Analysis: Mar 30, 2026", fontsize=14)
    plt.ylabel("Intraday % Change")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the analysis for the GitHub README
    plt.savefig('mar30_inflection.png')
    print("Visual Telemetry Exported: mar30_inflection.png")
    print(df[['Asset', 'Performance', 'Resilience_Delta']])

if __name__ == "__main__":
    generate_visual_telemetry()
