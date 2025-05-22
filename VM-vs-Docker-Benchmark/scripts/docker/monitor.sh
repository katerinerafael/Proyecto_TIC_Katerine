#!/bin/bash

echo "Iniciando shooter y monitoreo..."

# Ejecuta shooter en segundo plano
python3 shooter.py &

# Guarda PID
PID=$!

# Ejecuta monitor en paralelo
./benchmark &

# Espera que termine el shooter
wait $PID

echo "Todo terminado."
