
#!/bin/bash

START_TIME=$(date +%s)

timeout 10s python3 shooter.py &

GAME_PID=$!

wait $GAME_PID

END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo "Tiempo de ejecución: $ELAPSED segundos"
