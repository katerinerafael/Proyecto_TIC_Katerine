import pandas as pd
import matplotlib.pyplot as plt

def graficar(nombre, titulo, ylabel):
    # Leer los datos desde los archivos CSV
    df = pd.read_csv(f"datos/{nombre}.csv", header=None, names=["Iteración", "Valor"])

    # Crear la gráfica
    plt.figure()
    plt.plot(df["Iteración"], df["Valor"], marker='o')
    plt.title(titulo)
    plt.xlabel("Iteración")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(f"grafica_{nombre}.png")
    print(f"Gráfica guardada: grafica_{nombre}.png")

# Generar gráficas para cada métrica
graficar("cpu", "Uso de CPU", "CPU (%)")
graficar("ram", "Uso de RAM", "RAM (%)")
graficar("tiempo", "Tiempo de ejecución", "Segundos")
