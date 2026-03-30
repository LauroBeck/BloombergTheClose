#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

struct StockNode {
    std::string ticker;
    double roic;
    double wacc;
    bool is_infra; 
};

int main() {
    std::vector<StockNode> nodes = {
        {"NVDA", 32.5, 10.2, true},
        {"VRT",  18.2, 8.5,  true},
        {"PETR4", 15.2, 11.2, false}
    };

    double total_score = 0;
    for(auto& n : nodes) total_score += (n.roic - n.wacc) * (n.is_infra ? 1.5 : 1.0);

    std::cout << "--- V2: SOVEREIGNTY MULTIPLIER ---\n";
    for(auto& n : nodes) {
        double weight = (((n.roic - n.wacc) * (n.is_infra ? 1.5 : 1.0)) / total_score) * 100;
        printf("%-7s | Weight: %5.2f%% | Infra: %s\n", n.ticker.c_str(), weight, n.is_infra ? "YES" : "NO");
    }
    return 0;
}
