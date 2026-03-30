#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

/**
 * @brief V5: Stargate Sovereign Engine
 * Date: Mar 30, 2026 | 10Y Yield: 4.44% | Oil: $100
 */

struct Asset {
    std::string ticker;
    double roic;
    double wacc;
    bool is_sp100;     // S&P 100 Status (High Liquidity)
    bool is_infra;     // Sovereign Infra ($8T Trend)
};

void execute_stargate_flow(const std::vector<Asset>& universe, double treasury_yield) {
    std::cout << "--- V5: SOVEREIGN LIQUIDITY FLOW (MAR 30, 2026) ---" << std::endl;
    std::cout << "TICKER  | SPREAD | YIELD-ADJ ALPHA | SIGNAL" << std::endl;
    std::cout << "----------------------------------------------------" << std::endl;

    for (const auto& a : universe) {
        // Base Spread
        double spread = a.roic - a.wacc;
        
        // Alpha calculation: Penalize by current 4.44% Yield, Reward Sovereignty
        double yield_penalty = (treasury_yield / 10.0);
        double alpha = (spread - yield_penalty);
        
        if (a.is_sp100) alpha *= 1.25; // Liquidity Premium
        if (a.is_infra) alpha *= 1.50; // $8T Sovereign Multiplier

        std::string signal = (alpha > 15.0) ? "CORE" : (alpha < 0.0) ? "PURGE" : "ACCUM";

        printf("%-7s | %5.2f%% | %15.2f | %s\n", 
               a.ticker.c_str(), spread, alpha, signal.c_str());
    }
}

int main() {
    const double US10Y = 4.44; // Current 8-month high yield
    
    std::vector<Asset> target_universe = {
        {"NVDA",  32.5, 10.2, true,  true},  // Sovereign Anchor
        {"MU",    28.4, 9.5,  true,  true},  // S&P 100 New Titan
        {"VRT",   18.2, 8.5,  false, true},  // S&P 500 New Infra
        {"XOM",   14.1, 7.2,  true,  false}, // Energy Hedge
        {"PYPL",  9.1,  11.5, false, false}, // Removed from S&P 100
        {"PETR4", 15.2, 11.2, false, false}  // High-WACC tactical
    };

    execute_stargate_flow(target_universe, US10Y);
    return 0;
}
