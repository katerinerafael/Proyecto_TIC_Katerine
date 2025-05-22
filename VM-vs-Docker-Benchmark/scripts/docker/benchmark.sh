#!/bin/bash

echo "Iniciando benchmark..."

# CPU y RAM antes
cpu_start=$(top -b -n1 | grep "Cpu(s)" | awk '{print $2 + $4}')
ram_start=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
start_time=$(date +%s.%N)

# Ejecutar juego sin mostrar GUI
python3 shooter.py

# CPU y RAM después
cpu_end=$(top -b -n1 | grep "Cpu(s)" | awk '{print $2 + $4}')
ram_end=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
end_time=$(date +%s.%N)

cpu_avg=$(echo "($cpu_start + $cpu_end)/2" | bc -l)
ram_avg=$(echo "($ram_start + $ram_end)/2" | bc -l)
time_elapsed=$(echo "$end_time - $start_time" | bc)

# Guardar resultados
mkdir -p datos
echo "1,$cpu_avg" >> datos/cpu.csv
echo "1,$ram_avg" >> datos/ram.csv
echo "1,$time_elapsed" >> datos/tiempo.csv

echo "Benchmark completo. Resultados guardados en datos/"
