#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

struct Stock {
    std::string ticker;
    double roic;
    double wacc;
};

int main() {
    std::vector<Stock> portfolio = {
        {"MSFT", 21.54, 9.8}, 
        {"XOM", 14.1, 7.2}, 
        {"PYPL", 9.1, 11.5}
    };

    std::cout << "--- V1: FUNDAMENTAL SPREAD ANALYSIS ---\n";
    for (const auto& s : portfolio) {
        double spread = s.roic - s.wacc;
        printf("%-7s | Spread: %5.2f%% | Signal: %s\n", 
               s.ticker.c_str(), spread, (spread > 10 ? "CORE" : (spread < 0 ? "EXIT" : "HOLD")));
    }
    return 0;
}
