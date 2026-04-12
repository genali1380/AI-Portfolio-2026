# ✨ Reducción de Dimensionalidad: PCA y SVD Truncado

Este tutorial explora dos de las técnicas más potentes para la reducción de dimensionalidad en el aprendizaje automático: **Análisis de Componentes Principales (PCA)** y **Descomposición en Valores Singulares (SVD)**. A través de implementaciones prácticas, demostramos cómo estas técnicas permiten simplificar datos complejos mientras se preserva la información más relevante.

## ⚡ Accesos Rápidos

| Recurso | Descripción |
|---|---|
| 📓 **[Notebook: Tutorial PCA](./Tutorial_PCA.ipynb)** | Guía paso a paso sobre PCA y clasificación |
| 🌐 **[Reporte Web (PCA)](./Tutorial_PCA.html)** | Versión HTML del tutorial de PCA |
| 🔮 **[Simulación Interactiva SVD](./simulacion_recomendacion.html)** | Sistema de recomendación de películas en tiempo real |
| 🛠️ **[Script Generador](./generador_svd.py)** | Lógica de procesamiento de datos y construcción del modelo SVD |

---

## 🧪 Contenido del Tutorial

### 1. PCA: Clasificación de Cáncer de Mama
Utilizamos el dataset **Breast Cancer Wisconsin** (incluido en `scikit-learn`) para demostrar cómo PCA puede mejorar la eficiencia de un modelo de clasificación:
- **Reducción de ruido**: Eliminamos características redundantes para centrarnos en los componentes que explican la mayor varianza.
- **Visualización**: Proyectamos datos de alta dimensión en un espacio 2D para identificar clusters de tumores Benignos vs. Malignos.
- **Rendimiento**: Comparamos la precisión del modelo original frente al modelo optimizado con PCA.

### 2. SVD: Motor de Recomendación MovieLens
Implementamos un sistema de filtrado colaborativo basado en la descomposición de la matriz usuario-película del dataset **MovieLens 100K**:
- **Concepto**: El algoritmo descubre "preferencias latentes" (géneros implícitos, estilos de dirección) sin necesidad de etiquetas explícitas.
- **Simulación**: Una interfaz interactiva permite al usuario calificar películas y recibir recomendaciones instantáneas calculadas matemáticamente en el navegador.

---

## ⚙️ Lógica del Sistema de Recomendación

El motor de recomendación utiliza una versión optimizada de **SVD Truncado** para operar de forma ligera. La lógica reside en el script `generador_svd.py`:

> [!NOTE]
> El sistema sigue un proceso de 4 etapas:

1.  **Construcción de la Matriz**: Se crea una matriz $R$ de 943 usuarios por 1682 películas. Los valores faltantes se imputan con la media global.
2.  **Centrado de Datos**: Se resta la media de cada usuario para normalizar su tendencia de calificación (algunos usuarios son más generosos que otros).
3.  **Descomposición (Truncated SVD)**: Se descompone la matriz para extraer los $k=20$ componentes principales (V-transpose). Esto reduce la complejidad del sistema manteniendo la esencia de los datos.
4.  **Proyección y Reconstrucción**: 
    - El perfil del usuario se proyecta al espacio latente: $p_u = (r_u - \mu) \cdot V^T$.
    - Se reconstruyen las calificaciones predichas: $\hat{r} = (p_u \cdot V) + \mu$.

---

## 📊 Datasets Utilizados

- **Breast Cancer Wisconsin**: Características morfológicas de núcleos celulares.
- **MovieLens 100K**: 100,000 calificaciones de 1,682 películas por 943 usuarios.
  - `u.data`: Calificaciones brutas.
  - `u.item`: Metadatos de películas (títulos y géneros).

[⬅️ Volver al Portafolio](../../README.md)
