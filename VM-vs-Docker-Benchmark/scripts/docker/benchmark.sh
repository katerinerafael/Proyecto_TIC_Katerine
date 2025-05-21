#!/bin/bash

# Medir tiempo de ejecución del juego y guardarlo
START_TIME=$(date +%s)

# Ejecutar juego (puedes limitar tiempo con timeout para que no se quede infinito)
timeout 10s python3 shooter.py &

GAME_PID=$!

# Esperar que termine o timeout
wait $GAME_PID

END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

# Aquí podrías agregar comandos para extraer FPS, pero pygame lo muestra en pantalla.
# Alternativamente, puedes modificar shooter.py para que guarde FPS promedio en un archivo.

echo "Tiempo de ejecución: $ELAPSED segundos"
