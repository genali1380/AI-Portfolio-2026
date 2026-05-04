# ✨ Aprendizaje por Refuerzo y Multiple Testing en Sistemas Mecatrónicos

Este proyecto documenta la implementación de un agente de **Aprendizaje por Refuerzo Tabular (Q-Learning)** para optimizar las rutas de un Vehículo de Guiado Automático (AGV) en un entorno logístico simulado (`Taxi-v4` de Gymnasium). Además, se aplica rigor estadístico (**Multiple Testing**) para comparar diferentes configuraciones del modelo mediante pruebas de hipótesis, asegurando la validez de las mejoras en la política de aprendizaje.

## ⚡ Accesos Rápidos

| Recurso | Descripción |
|---|---|
| 📓 **[Notebook: Documentación Q-Learning](./AGV_QLearning_Doc.ipynb)** | Guía paso a paso sobre el entrenamiento del AGV y análisis estadístico |
| 🌐 **[Simulación Interactiva del Entrenamiento](./agv_training_replay.html)** | Interfaz HTML interactiva para reproducir y analizar los episodios del agente |

---

## 🧪 Contenido del Proyecto

### 1. Control del AGV con Q-Learning
Se utiliza el entorno `Taxi-v4` como representación de un almacén logístico donde un AGV debe aprender a navegar, recoger y entregar carga minimizando el tiempo y las penalizaciones.
- **Entrenamiento**: Se implementa el algoritmo Q-Learning tabular, permitiendo al agente descubrir la política óptima a lo largo de miles de iteraciones.
- **Convergencia**: Monitoreo de las recompensas promedio para determinar cuándo el sistema alcanza su máximo potencial operativo.
- **Sincronización Frame-Perfect**: Metodología para exportar el registro visual de los episodios directamente a una interfaz HTML, sin sufrir desincronizaciones por optimización de video (GIF).

### 2. Validación Estadística (Multiple Testing)
No basta con observar que un modelo parece aprender más rápido; se requiere evidencia estadística de que los diferentes hiperparámetros (como la tasa de aprendizaje $\alpha$) producen resultados significativamente distintos.
- **ANOVA Global**: Análisis de Varianza para detectar si existe alguna diferencia estadísticamente significativa en el desempeño entre distintas versiones del agente.
- **Corrección de Holm-Bonferroni**: Aplicación de pruebas T pareadas con ajustes para comparaciones múltiples, reduciendo la probabilidad de Falsos Positivos (Errores Tipo I) al comparar varias configuraciones del AGV.

---

## ⚙️ Entorno de Trabajo

> [!NOTE]
> A diferencia de otros enfoques basados en aprendizaje automático clásico (donde se provee un dataset estático), aquí la información es **generada dinámicamente** mediante la interacción del agente con su ambiente.

1. **Entorno Simulado (`Taxi-v4`)**: El agente percibe estados discretos (ubicación del AGV, destino, posiciones de obstáculos) y toma acciones para optimizar la recompensa futura.
2. **Visualización Reactiva**: El entrenamiento genera un historial de estados (checkpoints) empaquetados en un archivo JSON y reproducidos con precisión en la simulación web.

[⬅️ Volver al Portafolio](../../README.md)
