# 🎓 Modelo Predictivo de Rendimiento Académico

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completado-success?style=for-the-badge)
![Methodology](https://img.shields.io/badge/Metodología-Navaja_de_Ockham-orange?style=for-the-badge)

## 📊 Descripción del Proyecto
Este proyecto de ingeniería de datos desarrolla un modelo de regresión lineal robusto para predecir la calificación final (**$G3$**) de estudiantes de nivel secundaria/preparatoria.

El análisis se centra en aplicar el **Principio de Parsimonia**: en lugar de utilizar fuerza bruta con todas las variables disponibles, se aplicaron técnicas de selección de características (Forward Selection & Cross-Validation) para demostrar que un modelo simplificado (3 variables) puede ser igual de eficiente y más robusto que uno complejo.

### Fuente de Datos
Los datos provienen del **UCI Machine Learning Repository**, correspondientes al estudio de desempeño estudiantil en escuelas de Portugal (Cortez and Silva, 2008).
* 🔗 **Fuente Original:** [Student Performance Dataset](https://archive.ics.uci.edu/dataset/320/student+performance)

## 🗂️ Índice de Navegación
Para facilitar la revisión y reproducibilidad del estudio, los archivos se organizan de la siguiente manera:

* 🌐 [**Reporte Interactivo (Vista Web)**](./Reporte_Calificaciones.html): **Formato recomendado** para una lectura ejecutiva sin necesidad de correr código.
* 📓 [**Cuaderno Técnico (Jupyter Notebook)**](./Reporte_Calificaciones.ipynb): Documento completo con el código fuente, limpieza de datos (Tukey) y pruebas de validación.
* 💾 [**Base de Datos (CSV)**](./Calificaciones.csv): Dataset procesado utilizado para el entrenamiento del modelo.

---

## 📋 Características y Exploración de Datos
La base de datos original consta de **395 registros** de estudiantes de dos escuelas portuguesas (Gabriel Pereira y Mousinho da Silveira), capturando variables demográficas, sociales y académicas.

### Diccionario de Variables y Tipología
Uno de los retos principales del proyecto fue distinguir entre cómo Python lee un dato (*Tipo Computacional*) y qué representa realmente en el mundo real (*Tipo Estadístico*).

| Variable | Tipo Computacional | Tipo Estadístico | Descripción |
| :--- | :--- | :--- | :--- |
| **Escuela** | `Object` (String) | Cualitativa Nominal | Identificador de la escuela (GP o MS). |
| **Sexo** | `Object` (String) | Cualitativa Nominal | Género del estudiante (F o M). |
| **Edad** | `Int64` | Cuantitativa Discreta | Edad del estudiante (15-22 años). |
| **HorasDeEstudio**| `Int64` | **Cualitativa Ordinal** | Tiempo de estudio semanal (Escala 1 a 4). |
| **Reprobadas** | `Int64` | Cuantitativa Discreta | Número de clases reprobadas anteriormente. |
| **Internet** | `Object` (String) | Cualitativa Nominal | Acceso a internet en casa (yes/no). |
| **Faltas** | `Int64` | Cuantitativa Discreta | Número de ausencias escolares. |
| **G1, G2** | `Int64` | Cuantitativa Discreta | Calificaciones del primer y segundo periodo (0-20). |
| **G3** | `Int64` | **Variable Objetivo** | Calificación Final (Target) del curso. |

> ### 💡 Notas Técnicas de Ingeniería
> 1. **Transformación de `HorasDeEstudio`:** Aunque el dataset la entrega como número entero, estadísticamente no es lineal. Se trató como variable categórica (Dummy) para evitar sesgos en la regresión.
> 2. **Ceros Estructurales ($G3=0$):** Se detectó un subgrupo de alumnos con calificación final de 0. Estos casos se identificaron como **deserción escolar**. Se decidió conservarlos en el modelo para penalizar el riesgo real, aunque esto impacte levemente la métrica $R^2$ en el Test Set.
> 3. **Ingeniería de Características:** Se creó una variable sintética llamada `G_Promedio` (promedio de G1 y G2) para reducir la multicolinealidad.

## 🛠️ Herramientas Utilizadas
* **Lenguaje:** Python 3.9+
* **Procesamiento:** `Pandas` (Limpieza Tukey), `NumPy`.
* **Modelado:** `Scikit-Learn` (LinearRegression, RFECV, Cross-Validation).
* **Estadística:** `Statsmodels` (OLS para análisis de significancia P-Value).
* **Visualización:** `Seaborn` y `Matplotlib`.