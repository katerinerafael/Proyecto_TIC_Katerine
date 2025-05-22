# Evaluación Comparativa de Rendimiento: VM vs Docker

## 📌 Descripción del Proyecto

Este proyecto analiza comparativamente el rendimiento de una aplicación —un videojuego tipo shooter 2D desarrollado con tecnologías multiplataforma— ejecutada en dos entornos de virtualización distintos: **máquinas virtuales (VM)** y **contenedores Docker**.

El objetivo principal es evaluar el uso de recursos, los tiempos de respuesta y la eficiencia general del sistema en cada entorno, en un contexto realista y exigente a nivel computacional.

> Inicialmente se contempló el uso de un sistema físico basado en Arduino para esta evaluación, pero se optó por desarrollar el videojuego debido a la dificultad de obtener métricas de rendimiento precisas con hardware físico.

---

## 🧪 Metodología

Se construyeron dos entornos de prueba:

### 🐳 Docker
- Imagen oficial de Go utilizada para compilar y ejecutar el videojuego.
- Entorno aislado con herramientas de monitoreo integradas.
- Recursos equivalentes a los asignados en la VM.

### 🖥️ Máquina Virtual (VM)
- Plataforma: VirtualBox 7
- Sistema operativo: Ubuntu 22.04 (64-bit)
- Recursos asignados:
  - RAM: 9704 MB
  - Procesadores: 10 núcleos

### 💻 Host
- Procesador: Intel Core i5-12500H (12ª generación)
- RAM: 16 GB DDR4
- Almacenamiento: SSD 1TB
- Sistema operativo: Windows 11 Home

---

## 📊 Métricas Evaluadas

Durante la ejecución del videojuego se recolectaron las siguientes métricas:

- **Uso de CPU (%)**
- **Uso de RAM (MB)**
- **Tiempo de ejecución (segundos)**

---

## 🛠️ Tecnologías Utilizadas

- **Docker**: Contenedores ligeros y portables.
- **VirtualBox**: Virtualización de sistemas operativos completos.
- **Go (Golang)**: Lenguaje de programación del videojuego.
- **Python**: Herramientas de análisis y visualización de datos.
- **Ubuntu**: Sistema operativo para la VM.

---

## 🎮 Aplicación: Shooter 2D

El videojuego actúa como carga de trabajo representativa al involucrar procesamiento gráfico, eventos concurrentes, colisiones y lógica de juego. Es ideal para evaluar el rendimiento de cada entorno de virtualización bajo condiciones exigentes.

---

## 📈 Resultados y Gráficas

Los resultados indican diferencias claras entre ambos entornos:

### Docker
- ✅ Tiempo de ejecución bajo y constante.
- ✅ Uso de RAM estable (35%).
- ✅ Uso de CPU controlado, con picos manejables.
- 🔸 Ligereza, escalabilidad y eficiencia destacadas.

### VM
- ✅ RAM extremadamente baja (posiblemente por limitaciones del monitoreo).
- ✅ Mayor aislamiento del entorno.
- ❌ Tiempo de ejecución significativamente más alto (~26s).
- ❌ Uso de CPU más errático y potencialmente elevado.

---

## 📌 Conclusiones

- **Docker** se presenta como la mejor opción para cargas de trabajo que requieren eficiencia, velocidad de ejecución y portabilidad. Ideal para aplicaciones puramente de software.
- **Máquinas virtuales** siguen siendo útiles cuando se necesita:
  - Aislamiento total.
  - Compatibilidad con hardware embebido.
  - Emulación de sistemas operativos completos.

> 📚 Para más detalles técnicos y visualizaciones, consulta el informe completo:  
https://docs.google.com/document/d/1qOZyaTSgXH7RfiJsBEsQH4FRpacJ8OQ31AOqG6OaHc8/edit?usp=sharing

---

