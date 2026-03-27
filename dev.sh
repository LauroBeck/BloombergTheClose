#!/bin/bash
# 2026 Telemetry Hot-Swap Pipeline

FILE="monitor.cpp"
EXE="alpha_monitor"

# 1. Edit the source (fast text-replace or full rewrite)
nano "$FILE"

# 2. Compile with C++20 and Maximum Optimization
g++ -O3 -std=c++20 "$FILE" -o "$EXE"

# 3. Execution & Validation
if [ $? -eq 0 ]; then
    echo -e "\033[1;32mBuild Success. Launching Telemetry...\033[0m"
    ./"$EXE"
else
    echo -e "\033[1;31mBuild Failed. Check syntax in $FILE\033[0m"
fi
