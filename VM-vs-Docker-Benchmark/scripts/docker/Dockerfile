# Usa imagen oficial de Go
FROM golang:1.21

# Instala dependencias
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Instala matplotlib y pandas
RUN pip3 install pandas matplotlib

# Instala gopsutil para monitoreo
RUN go install github.com/shirou/gopsutil/v3@latest

# Copia archivos
WORKDIR /app
COPY main.go .

# Compila el binario
RUN go mod init benchmark && go mod tidy && go build -o benchmark

# Ejecuta el binario al correr el contenedor
CMD ["./benchmark"]
