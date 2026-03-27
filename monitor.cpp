#include <iostream>
#include <vector>
#include <iomanip>
#include <string>

struct AlphaTelemetry {
    std::string asset;
    double close;
    double delta;
    std::string status;
};

int main() {
    // Bloomberg "The Close" - Verified Friday, March 27, 2026
    // US Stocks worst week since Iran war began; 5th straight losing week.
    std::vector<AlphaTelemetry> report = {
        {"NASDAQ_COMP", 20948.36, -2.15, "CORRECTION"}, 
        {"S&P_500", 6375.85, -1.67, "BEAR_THREAT"},
        {"DOW_JONES", 45166.64, -1.73, "WEEKLY_LOW"},
        {"PANW", 147.02, -5.97, "SECTOR_LOW"},    // Session low hit $143.50
        {"WTI_CRUDE", 99.26, 5.06, "WAR_PREMIUM"},  // Near $100 psychological
        {"BRENT_OIL", 112.49, 4.14, "SUPPLY_SHOCK"}, // 7% intraday surge
        {"GOLD_SPOT", 4518.37, 3.30, "SAFE_HAVEN"}  
    };

    std::cout << "\033[1;34m--- ALPHA FOX QUANT: FINAL SESSION SYNC [03/27/2026] ---\033[0m" << std::endl;
    std::cout << std::left << std::setw(15) << "ASSET" << std::setw(12) << "CLOSE" << std::setw(10) << "DELTA %" << "STATUS" << std::endl;
    std::cout << "------------------------------------------------------------" << std::endl;

    for (const auto& item : report) {
        std::string color = (item.delta < 0) ? "\033[1;31m" : "\033[1;32m";
        std::cout << std::left << std::setw(15) << item.asset 
                  << std::setw(12) << std::fixed << std::setprecision(2) << item.close 
                  << color << (item.delta > 0 ? "+" : "") << std::setw(9) << item.delta << "%\033[0m " 
                  << item.status << std::endl;
    }
    
    std::cout << "\n\033[1;33mINTEL: Arak & Yazd nuclear sites hit. Iran vowing 'Heavy Price'.\033[0m" << std::endl;
    std::cout << "\033[1;31mURGENT: VIX hits 31.05. Brent +54% YTD. Hormuz deadline Apr 6.\033[0m" << std::endl;
    return 0;
}
