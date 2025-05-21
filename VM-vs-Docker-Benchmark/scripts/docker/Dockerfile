# Usar una imagen base con Python
FROM python:3.9-slim

# Instalar dependencias necesarias para pygame (SDL y otras)
RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libsmpeg-dev \
    libportmidi-dev \
    libavformat-dev \
    libswscale-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de la app
WORKDIR /app

# Copiar requirements y el juego
COPY ../../app_test/shooter/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ../../app_test/shooter/ ./

# Copiar script benchmark.sh y darle permisos
COPY benchmark.sh /app/
RUN chmod +x /app/benchmark.sh

# Comando por defecto para correr el benchmark
CMD ["./benchmark.sh"]

