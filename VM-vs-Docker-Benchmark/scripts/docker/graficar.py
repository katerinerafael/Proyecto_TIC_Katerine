import pandas as pd
import matplotlib.pyplot as plt

def graficar(nombre, titulo, ylabel):
    df = pd.read_csv(f"datos/{nombre}.csv", header=None, names=["Iteración", "Valor"])
    plt.figure()
    plt.plot(df["Iteración"], df["Valor"], marker='o')
    plt.title(titulo)
    plt.xlabel("Iteración")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(f"grafica_{nombre}.png")
    print(f"Gráfica guardada: grafica_{nombre}.png")

def graficar_conjunto():
    cpu = pd.read_csv("datos/cpu.csv", header=None, names=["Iteración", "CPU"])
    ram = pd.read_csv("datos/ram.csv", header=None, names=["Iteración", "RAM"])
    tiempo = pd.read_csv("datos/tiempo.csv", header=None, names=["Iteración", "Tiempo"])

    plt.figure()
    plt.plot(cpu["Iteración"], cpu["CPU"], label="CPU (%)")
    plt.plot(ram["Iteración"], ram["RAM"], label="RAM (%)")
    plt.plot(tiempo["Iteración"], tiempo["Tiempo"], label="Tiempo (s)")
    plt.title("Métricas en conjunto")
    plt.xlabel("Iteración")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(True)
    plt.savefig("grafica_conjunta.png")
    print("Gráfica guardada: grafica_conjunta.png")

graficar("cpu", "Uso de CPU", "CPU (%)")
graficar("ram", "Uso de RAM", "RAM (%)")
graficar("tiempo", "Tiempo de ejecución", "Segundos")
graficar_conjunto()
