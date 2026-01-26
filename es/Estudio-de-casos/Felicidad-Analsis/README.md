# 🌍 Análisis Econométrico: Determinantes de la Felicidad Global

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completado-success?style=for-the-badge)

## 📊 Descripción del Proyecto
Este proyecto presenta un análisis estadístico e inferencial diseñado para responder una interrogante clásica de la economía conductual: **¿El dinero compra la felicidad?**

El estudio parte de una exploración inicial entre el Producto Interno Bruto (GDP) y la Felicidad reportada, para luego expandirse hacia un **Modelo de Regresión Múltiple**. El objetivo es contrastar si el ingreso económico por sí solo es suficiente para predecir el bienestar de una nación, o si pierde relevancia al considerar factores sociales más humanos como la salud, la libertad y el apoyo social.

## 📂 Origen y Procesamiento de Datos
Para construir el dataset final, se realizó una integración (Data Merging) de dos fuentes, aplicando técnicas de limpieza de texto para maximizar la coincidencia de países:

1.  **Dataset Base:** Iniciamos con **141 países**, cruzando el *Índice de Felicidad (2022)* con el *GDP (2020)* para capturar el impacto económico post-pandemia.
2.  **Dataset Extendido (Fuente Externa):** Se incorporó el *World Happiness Report 2022* (Fuente: [Kaggle](https://worldhappiness.report/ed/2022/)), el cual contenía **146 registros**.
3.  **Muestra Final:** Tras la homologación de nombres y el cruce de bases de datos, el análisis final se consolidó con una muestra de **139 países** (intersección válida entre ambas fuentes).

## 🗂️ Índice de Navegación
Para facilitar la revisión del portafolio, los recursos se encuentran disponibles en los siguientes formatos:

* 🌐 [**Reporte Interactivo (Vista Web)**](./Reporte_Analisis.html): **Formato recomendado** para una lectura fluida en el navegador.
* 📓 [**Cuaderno Técnico (Jupyter Notebook)**](./Reporte_Analisis.ipynb): Código fuente completo con metodología y pruebas estadísticas.
* 💾 [**Datos Económicos (CSV)**](./Felicidad_y_GDP.csv): Archivo base utilizado para la regresión simple.
* 💾 [**Datos Sociales (CSV)**](./World_Happiness_Report_2022.csv): Archivo complementario para la regresión múltiple.

---

## 📋 Diccionario de Variables
A continuación se detallan las características técnicas de las variables empleadas en el modelo final:

| Variable | Tipo Computacional | Tipo Estadístico | Descripción |
| :--- | :--- | :--- | :--- |
| **Felicidad** | `Float64` | Cuantitativa Continua | **Variable Objetivo (Target).** Puntaje en la Escalera de Cantril (0-10). |
| **GDP** | `Float64` | Cuantitativa Continua | Producto Interno Bruto per cápita (Valores nominales 2020). |
| **Social Support** | `Float64` | Cuantitativa Continua | Promedio nacional de percepción de apoyo social. |
| **Life Expectancy** | `Float64` | Cuantitativa Continua | Esperanza de vida saludable al nacer (en años). |
| **Freedom** | `Float64` | Cuantitativa Continua | Índice de libertad para tomar decisiones de vida. |
| **Generosity** | `Float64` | Cuantitativa Continua | Disposición de la población a realizar donaciones. |

> ### 💡 Nota Técnica sobre Transformaciones
> Debido a la naturaleza exponencial de la economía global, la variable **`GDP`** fue sometida a una transformación logarítmica (`np.log`) dentro del notebook. Esto convierte su tipo estadístico a una escala linealizada para cumplir con los supuestos de la regresión OLS.

---

## 🛠️ Herramientas Utilizadas
* **Lenguaje:** Python 3.14.2
* **Librerías:** `Pandas` (Limpieza y Merging), `Statsmodels` (Inferencia Estadística), `Matplotlib` & `Seaborn` (Visualización).
* **Técnicas:** Regresión Lineal (Simple y Múltiple), Prueba de Shapiro-Wilk, Partial F-Test.
