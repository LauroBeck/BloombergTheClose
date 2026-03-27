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
    // Market Impact: 5th straight losing week; Nasdaq in official correction.
    std::vector<AlphaTelemetry> report = {
        {"NASDAQ", 20948.36, -2.10, "CORRECTION"}, 
        {"S&P 500", 6368.85, -1.70, "YEARLY_LOW"},
        {"DOW JONES", 45166.64, -1.70, "BEAR_THREAT"},
        {"PANW", 144.14, -7.82, "SECTOR_LOW"},   // Hit $143.50 intraday low
        {"WTI_CRUDE", 99.64, 5.50, "WAR_PREMIUM"}, // Settlement high near $100
        {"BRENT_OIL", 105.32, 3.40, "SUPPLY_SHOCK"},
        {"GOLD_SPOT", 4510.43, 2.98, "SAFE_HAVEN"}  
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
    
    std::cout << "\n\033[1;33mINTEL: Arak/Yazd facilities hit. Iran rejects 15-point plan.\033[0m" << std::endl;
    std::cout << "\033[1;33mDEADLINE: Hormuz clearance extended to April 6 (8:00 PM ET).\033[0m" << std::endl;
    return 0;
}
