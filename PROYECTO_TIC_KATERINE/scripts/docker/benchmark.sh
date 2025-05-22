#!/bin/bash

echo "Iniciando benchmark..."

mkdir -p datos
chmod 777 datos

cpu_start=$(top -b -n1 | awk '/%Cpu/ {print 100 - $8}')
ram_start=$(free | awk '/Mem:/ {print $3/$2 * 100.0}')
start_time=$(date +%s.%N)

python3 shooter.py

cpu_end=$(top -b -n1 | awk '/%Cpu/ {print 100 - $8}')
ram_end=$(free | awk '/Mem:/ {print $3/$2 * 100.0}')
end_time=$(date +%s.%_
