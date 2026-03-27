#!/bin/bash
# 2026 Telemetry Hot-Swap & GitHub Sync Pipeline

FILE="monitor.cpp"
EXE="alpha_monitor"
REPO_URL="https://github.com/LauroBeck/BloombergTheClose.git"

# 1. Compile with C++20 and Maximum Optimization
echo -e "\033[1;33mBuilding $FILE...\033[0m"
g++ -O3 -std=c++20 "$FILE" -o "$EXE"

# 2. Execution & Validation
if [ $? -eq 0 ]; then
    clear
    ./"$EXE"
    
    # 3. Optional GitHub Sync
    echo -e "\n\033[1;36mBuild Successful. Sync to GitHub? (y/n)\033[0m"
    read -r sync_choice
    if [ "$sync_choice" == "y" ]; then
        git add "$FILE"
        git commit -m "Telemetry Update: $(date +'%Y-%m-%d %H:%M') Market Shift"
        git push origin main
        echo -e "\033[1;32mRepository Updated.\033[0m"
    fi
else
    echo -e "\n\033[1;31mBuild Failed. Check syntax in $FILE\033[0m"
fi
