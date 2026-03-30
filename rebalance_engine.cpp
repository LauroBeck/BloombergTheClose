#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>

/**
 * @brief Macro-Geopolitical Rebalancing Engine
 * Data: Mar 30, 2026 | Crude: $100/bbl | S&P: 5-Week Loss Streak
 */

struct StockNode {
    std::string ticker;
    double roic;
    double wacc;
    double energy_beta; // Sensitivity to $100 oil
    bool is_infra;      // Vertiv/Lumentum/Semi Sovereignty
};

void run_telemetry(const std::vector<StockNode>& portfolio, double geo_risk_factor) {
    std::cout << "--- MARCH 30, 2026: STAGFLATION REBALANCE PROTOCOL ---" << std::endl;
    std::cout << "TICKER  | SPREAD | RISK-ADJ WT | SIGNAL" << std::endl;
    std::cout << "----------------------------------------------------" << std::endl;

    double total_score = 0;
    for (const auto& s : portfolio) {
        // Core Logic: ROIC-WACC Spread + Energy Beta Adjustment
        double score = (s.roic - s.wacc) + (s.energy_beta * geo_risk_factor);
        if (s.is_infra) score *= 1.25; // Sovereignty Premium
        total_score += std::max(0.1, score);
    }

    for (const auto& s : portfolio) {
        double score = (s.roic - s.wacc) + (s.energy_beta * geo_risk_factor);
        if (s.is_infra) score *= 1.25;
        
        double weight = (std::max(0.1, score) / total_score) * 100.0;
        std::string signal = (weight > 25.0) ? "STRONG BUY" : (weight < 5.0) ? "EXIT" : "HOLD";

        printf("%-7s | %5.1f%% | %10.2f%% | %s\n", 
               s.ticker.c_str(), (s.roic - s.wacc), weight, signal.c_str());
    }
}

int main() {
    // Geopolitical Risk Factor: High (Due to Persian Gulf instability)
    const double GEO_RISK = 0.85;

    std::vector<StockNode> active_market = {
        {"NVDA",  32.5, 10.2, -0.2, true},  // Tech Sovereignty
        {"VRT",   18.2, 8.5,  -0.1, true},  // AI Infra (New Addition)
        {"XOM",   14.1, 7.2,   0.9, false}, // Energy Hedge (High Beta to Oil)
        {"LITE",  12.4, 9.1,  -0.1, true},  // New Addition (Photonics)
        {"PETR4", 15.2, 11.2,  1.1, false}, // BR Energy (Extreme Oil Beta)
        {"PYPL",  9.1,  11.5, -0.4, false}  // Removed from S&P 100 (Mar 23)
    };

    run_telemetry(active_market, GEO_RISK);
    return 0;
}
