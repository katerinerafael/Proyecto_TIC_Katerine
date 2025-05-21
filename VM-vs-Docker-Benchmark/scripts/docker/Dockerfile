# Usamos una imagen base de Python
FROM python:3.9-slim

# Instalamos las dependencias necesarias
RUN apt-get update && apt-get install -y \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos del proyecto
COPY . /app

# Instalamos las dependencias de Python
RUN pip install -r requirements.txt

# Exponemos el puerto (si es necesario)
EXPOSE 8080

# Comando para ejecutar el script principal o el juego
CMD ["python3", "shooter.py"]
