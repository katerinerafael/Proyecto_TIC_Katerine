import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(path, nombre):
    df = pd.read_csv(f"{path}/{nombre}.csv", header=None, names=["Iteración", "Valor"])
    return df

def comparar_metrica(nombre, ylabel, titulo):
    vm = cargar_datos("datos_vm", nombre)
    docker = cargar_datos("datos_docker", nombre)

    plt.figure(figsize=(10,6))
    plt.plot(vm["Iteración"], vm["Valor"], label="Máquina Virtual")
    plt.plot(docker["Iteración"], docker["Valor"], label="Docker")
    plt.title(titulo)
    plt.xlabel("Iteración")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.savefig(f"comparativa_{nombre}.png")
    print(f"Gráfica comparativa guardada: comparativa_{nombre}.png")

comparar_metrica("cpu", "Uso de CPU (%)", "Comparativa de Uso de CPU")
comparar_metrica("ram", "Uso de RAM (%)", "Comparativa de Uso de RAM")
comparar_metrica("tiempo", "Tiempo (s)", "Comparativa de Tiempo de Ejecución")
