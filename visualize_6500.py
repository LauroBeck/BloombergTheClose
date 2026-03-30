import matplotlib.pyplot as plt
import datetime

def generate_6500_projection():
    # Data points for the projection
    dates = ['Mar 30 (Now)', 'Apr 1', 'Apr 3', 'Apr 6 (Target)']
    prices = [6343.72, 6390.00, 6445.00, 6500.00]
    
    plt.figure(figsize=(10, 6), facecolor='#f4f4f4')
    
    # Plot the Recovery Path
    plt.plot(dates, prices, marker='o', linestyle='-', color='#007acc', linewidth=3, label='Recovery Trajectory')
    
    # Highlight the 6,500 Breakout Line
    plt.axhline(y=6500, color='green', linestyle='--', linewidth=2, label='6,500 Bullish Pivot')
    
    # Shading the "Opportunity Zone"
    plt.fill_between(dates, 6343.72, 6500, color='green', alpha=0.1)

    # Formatting the "Pro View"
    plt.title(f"S&P 500 Recovery Projection: The Path to 6,500", fontsize=14, fontweight='bold')
    plt.ylabel("S&P 500 Index Points")
    plt.ylim(6300, 6550)
    plt.grid(axis='y', linestyle=':', alpha=0.6)
    
    # Annotations for the README
    plt.annotate('April 6 Breakthrough', xy=('Apr 6 (Target)', 6500), xytext=('Apr 1', 6520),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1))
    
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig('spx_6500_projection.png')
    print("Recovery Projection Generated: spx_6500_projection.png")

if __name__ == "__main__":
    generate_6500_projection()
