#!/bin/bash

# Archivo de salida para las métricas
CPU_FILE="/app/datos/cpu.csv"
RAM_FILE="/app/datos/ram.csv"
TIME_FILE="/app/datos/tiempo.csv"

# Limpiar archivos existentes antes de comenzar
> $CPU_FILE
> $RAM_FILE
> $TIME_FILE

# Función para capturar métricas de CPU, RAM y tiempo
get_metrics() {
    # Captura del tiempo inicial
    start_time=$(date +%s)

    # Medición de la CPU y RAM antes de ejecutar el juego
    cpu_before=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    ram_before=$(free | grep Mem | awk '{print $3/$2 * 100.0}')

    # Ejecutar el juego o el script de prueba
    python3 /app/shooter.py

    # Medición de la CPU y RAM después de ejecutar el juego
    cpu_after=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    ram_after=$(free | grep Mem | awk '{print $3/$2 * 100.0}')

    # Captura del tiempo final
    end_time=$(date +%s)

    # Cálculo del tiempo de ejecución
    execution_time=$((end_time - start_time))

    # Escribir las métricas en los archivos CSV
    echo "$cpu_before,$cpu_after" >> $CPU_FILE
    echo "$ram_before,$ram_after" >> $RAM_FILE
    echo "$execution_time" >> $TIME_FILE
}

# Ejecutar las métricas varias veces para tener suficientes datos
for i in {1..10}
do
    get_metrics
    sleep 1  # Pausa de 1 segundo entre ejecuciones
done

echo "Benchmark completo. Los resultados están guardados en /app/datos."
