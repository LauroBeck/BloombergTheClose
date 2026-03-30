import matplotlib.pyplot as plt
import datetime

def generate_inflection_graph():
    # March 30, 2026 Telemetry Data
    spx_current = 6343.72
    projected_inflection = 6289.54
    hard_floor = 6145.00
    
    levels = [spx_current, projected_inflection, hard_floor]
    labels = ['Current Level (6343.72)', 'Projected Inflection (6289.54)', 'Institutional Floor (6145.00)']
    colors = ['#1f77b4', '#ff7f0e', '#d62728']

    plt.figure(figsize=(10, 7), facecolor='#f0f0f0')
    
    # Create the Bar Chart
    bars = plt.bar(labels, levels, color=colors, alpha=0.85, width=0.6)
    
    # Add Price Labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 20, f'{yval:,.2f}', 
                 ha='center', va='bottom', fontweight='bold', fontsize=11)

    # Highlight the "Buffer Zone"
    plt.axhline(y=hard_floor, color='red', linestyle='--', alpha=0.6, label='Hard Support Line')
    plt.fill_between([-0.5, 2.5], hard_floor, spx_current, color='green', alpha=0.05, label='2.28% Buffer Zone')

    # Formatting
    plt.title(f"S&P 500 Structural Gravity Analysis | {datetime.date.today()}", fontsize=14, fontweight='bold', pad=20)
    plt.ylabel("Index Points", fontsize=12)
    plt.ylim(5800, 6500) # Zoomed in on the inflection zone
    plt.grid(axis='y', linestyle=':', alpha=0.5)
    
    # Strategic Annotation
    plt.annotate('April 6 Risk Window', xy=(1, projected_inflection), xytext=(1.5, 6400),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))

    plt.tight_layout()
    plt.savefig('spx_inflection_graph.png')
    print("Graph Generated: spx_inflection_graph.png")

if __name__ == "__main__":
    generate_inflection_graph()
