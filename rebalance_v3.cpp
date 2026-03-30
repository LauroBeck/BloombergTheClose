#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>

struct StockNode {
    std::string ticker;
    double roic;
    double wacc;
    double energy_beta; 
    bool is_infra;      
};

void run_telemetry(const std::vector<StockNode>& portfolio, double geo_risk_factor) {
    std::cout << "--- V3: STAGFLATION REBALANCE (MAR 30, 2026) ---\n";
    std::cout << "TICKER  | SPREAD | RISK-ADJ WT | SIGNAL\n";
    std::cout << "----------------------------------------------\n";

    double total_score = 0;
    for (const auto& s : portfolio) {
        double score = (s.roic - s.wacc) + (s.energy_beta * geo_risk_factor);
        if (s.is_infra) score *= 1.25; 
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
    const double GEO_RISK = 0.85; // High Risk: Persian Gulf / Strait of Hormuz
    std::vector<StockNode> active_market = {
        {"NVDA",  32.5, 10.2, -0.2, true},  
        {"VRT",   18.2, 8.5,  -0.1, true},  
        {"XOM",   14.1, 7.2,   0.9, false}, 
        {"LITE",  12.4, 9.1,  -0.1, true},  
        {"PETR4", 15.2, 11.2,  1.1, false}, 
        {"PYPL",  9.1,  11.5, -0.4, false}  
    };

    run_telemetry(active_market, GEO_RISK);
    return 0;
}
