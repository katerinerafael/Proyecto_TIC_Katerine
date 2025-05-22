// main.go
package main

import (
    "fmt"
    "os"
    "time"

    "github.com/shirou/gopsutil/v3/cpu"
    "github.com/shirou/gopsutil/v3/mem"
)

func guardarDatos(nombre string, datos []float64) {
    os.MkdirAll("datos", os.ModePerm)
    f, err := os.Create("datos/" + nombre + ".csv")
    if err != nil {
        panic(err)
    }
    defer f.Close()

    for i, d := range datos {
        fmt.Fprintf(f, "%d,%.2f\n", i, d)
    }
}

func main() {
    var cpuUsos, ramUsos, tiempos []float64

    fmt.Println("Inicio del monitoreo...")
    for i := 0; i < 10; i++ {
        start := time.Now()

        cpuPorcentaje, _ := cpu.Percent(0, false)
        memInfo, _ := mem.VirtualMemory()

        // Simula trabajo
        time.Sleep(300 * time.Millisecond)

        duracion := time.Since(start).Seconds()

        cpuUsos = append(cpuUsos, cpuPorcentaje[0])
        ramUsos = append(ramUsos, memInfo.UsedPercent)
        tiempos = append(tiempos, duracion)

        fmt.Printf("Iteración %d - CPU: %.2f%%, RAM: %.2f%%, Tiempo: %.2fs\n",
            i, cpuPorcentaje[0], memInfo.UsedPercent, duracion)
    }
    
    guardarDatos("cpu", cpuUsos)
    guardarDatos("ram", ramUsos)
    guardarDatos("tiempo", tiempos)

    fmt.Println("Datos guardados en la carpeta datos/")
}
