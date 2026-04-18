# ✨ Agrupamiento: K-Means y Clustering Jerárquico

Este tutorial explora dos de las técnicas más potentes para el análisis de datos no supervisado: **K-Means** y **Clustering Jerárquico**. A través de implementaciones prácticas, demostramos cómo estas técnicas permiten descubrir estructuras ocultas y agrupaciones naturales dentro de conjuntos de datos.

## ⚡ Accesos Rápidos

| Recurso | Descripción |
|---|---|
| 📓 **[Notebook: Tutorial Clustering](./tutorial_clustering.ipynb)** | Guía paso a paso sobre K-Means y Jerárquico |
| 🌐 **[Reporte Web (Clustering)](./tutorial_clustering.html)** | Versión HTML del tutorial interactivo |
| 💾 **[Dataset Sintético](./synthetic_blobs.csv)** | Datos bidimensionales generados (blobs) |

---

## 🧪 Contenido del Tutorial

### 1. Entendiendo la Lógica de K-Means
Utilizamos un conjunto de datos **sintético** (`synthetic_blobs.csv`) para ilustrar los fundamentos geométricos del clustering particional. Este dataset artificial fue diseñado específicamente para demostrar cómo K-Means iterativamente:
- **Asigna Puntos**: Minimiza la distancia euclidiana hacia el centroide de cada grupo.
- **Actualiza Centroides**: Recalcula el centro de gravedad tras reasignar las observaciones.
- **Convergencia**: Se observa el proceso y los hiperparámetros que le dan fin.

### 2. Clustering Jerárquico y Dendrogramas
Implementamos técnicas de agrupamiento aglomerativo (bottom-up) que no requieren definir la cantidad de clusters a priori.
- **Enfoque Aglomerativo**: Análisis paso a paso de la creación incremental de grupos.
- **Dendrogramas**: Visualizamos el árbol de agrupaciones sucesivas, interpretando cómo seleccionar la distancia de corte.

---

## 📊 Datasets Utilizados

- **Synthetic Blobs** (`synthetic_blobs.csv`): Conjunto de datos de coordenadas generadas procedimentalmente, proporcionando clústeres esféricos bien definidos ideales para una calibración inicial de herramientas de clustering.

[⬅️ Volver al Portafolio](../../README.md)
