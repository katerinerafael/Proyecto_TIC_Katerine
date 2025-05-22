import pandas as pd
import matplotlib.pyplot as plt

# Función para graficar los datos individuales
def graficar_individual(nombre, titulo, ylabel):
    df = pd.read_csv(f"datos/{nombre}.csv", header=None, names=["Iteración", "Valor"])
    plt.figure(figsize=(10, 6))
    plt.plot(df["Iteración"], df["Valor"], marker='o')
    plt.title(titulo)
    plt.xlabel("Iteración")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(f"grafica_{nombre}.png")
    print(f"Gráfica individual guardada: grafica_{nombre}.png")

# Función para graficar los tres datos en conjunto
def graficar_conjunto():
    # Leer los tres archivos CSV
    df_cpu = pd.read_csv("datos/cpu.csv", header=None, names=["Iteración", "CPU"])
    df_ram = pd.read_csv("datos/ram.csv", header=None, names=["Iteración", "RAM"])
    df_tiempo = pd.read_csv("datos/tiempo.csv", header=None, names=["Iteración", "Tiempo"])

    # Crear la figura para la gráfica combinada
    plt.figure(figsize=(10, 6))

    # Graficar los tres conjuntos de datos en el mismo gráfico
    plt.plot(df_cpu["Iteración"], df_cpu["CPU"], marker='o', label="Uso de CPU (%)")
    plt.plot(df_ram["Iteración"], df_ram["RAM"], marker='s', label="Uso de RAM (%)")
    plt.plot(df_tiempo["Iteración"], df_tiempo["Tiempo"], marker='^', label="Tiempo de ejecución (Segundos)")

    # Títulos y etiquetas
    plt.title("Comparación de Uso de CPU, RAM y Tiempo de Ejecución")
    plt.xlabel("Iteración")
    plt.ylabel("Valor")
    plt.grid(True)

    # Añadir leyenda
    plt.legend()

    # Guardar la gráfica combinada
    plt.savefig("grafica_completa.png")
    print("Gráfica combinada guardada: grafica_completa.png")

# Graficar individualmente para CPU, RAM y Tiempo
graficar_individual("cpu", "Uso de CPU", "CPU (%)")
graficar_individual("ram", "Uso de RAM", "RAM (%)")
graficar_individual("tiempo", "Tiempo de ejecución", "Segundos")

# Graficar los tres en conjunto
graficar_conjunto()
