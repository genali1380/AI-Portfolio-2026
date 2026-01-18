# Estudio Multidimensional sobre Factores de Riesgo en la Obesidad Latinoamericana

## 📊 Descripción del Proyecto
Este proyecto presenta un análisis estadístico e inferencial sobre datos recopilados en poblaciones de **México, Perú y Colombia**. El objetivo principal es identificar los patrones de estilo de vida y factores demográficos que tienen una correlación directa con los niveles de obesidad, proporcionando una visión basada en datos sobre este reto de salud pública.

La base de datos utilizada es una versión simplificada del dataset original, que viene de parte de UCI Machine Learning Repository; el dataset original se encuentra en el siguiente enlace: https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition

## 🗂️ Índice de Navegación del Proyecto

Para facilitar la revisión del estudio, los recursos se presentan en los siguientes formatos:

* 🌐 [**Reporte Interactivo (Vista Web)**](./Reporte_Análisis.html): **Formato recomendado** para una lectura fluida en el navegador.
* 📓 [**Cuaderno Técnico (Jupyter Notebook)**](./Reporte_Análisis.ipynb): Documento con el código fuente completo y metodología para fines de reproducibilidad.
* 💾 [**Datos del Estudio (CSV)**](./Obesity_Data.csv): Base de datos con los registros analizados de México, Perú y Colombia.

## 📋 Características del Conjunto de Datos
La base de datos se compone de información recolectada de 2,111 individuos, capturando una mezcla diversa de perfiles físicos y hábitos de comportamiento.

### Estructura y Alcance
Volumen: 2,111 registros con 10 variables cada uno.
Origen: Estudio multicéntrico realizado en México, Perú y Colombia.
Naturaleza de los Datos: El dataset combina variables numéricas (mediciones físicas) y categóricas (hábitos y etiquetas descriptivas).

### Diccionario de Variables

| Variable | Tipo | Descripción |
| :--- | :--- | :--- |
| **Sexo** | Categórica | Género biológico del participante. |
| **Edad** | Numérica | Edad cronológica (rango observado de 14 a 61 años). |
| **Estatura** | Numérica | Altura en metros. |
| **Peso** | Numérica | Masa corporal en kilogramos. |
| **FamiliarConSobrepeso** | Categórica | Antecedentes familiares directos de obesidad. |
| **ComeMuchasCalorias** | Categórica | Ingesta frecuente de alimentos con alta densidad calórica. |
| **ComeVegetales** | Numérica | Frecuencia reportada de consumo de vegetales. |
| **Fumador** | Categórica | Identifica si el individuo posee el hábito de tabaquismo. |
| **ConsumoDeAgua** | Numérica | Consumo diario de agua ingerida. |
| **NivelDeObesidad** | Categórica | **Variable Objetivo:** Clasificación basada en el IMC. |

> ### 💡 Nota Técnica sobre las Variables
> Las variables **`ComeVegetales`** y **`ConsumoDeAgua`** se presentan en este conjunto de datos como valores numéricos continuos (con decimales). Es importante aclarar que, en el diseño original del estudio, estas representan niveles de frecuencia en una escala del **1 al 3**. La presencia de decimales es resultado de técnicas de preprocesamiento y aumento de datos (como SMOTE) aplicadas para balancear el set, por lo que deben interpretarse como indicadores de tendencia dentro de dichos niveles ordinales.

## 🛠️ Herramientas Utilizadas
* **Lenguaje:** Python 3.14.2
* **Bibliotecas:** Pandas (manejo de datos), Matplotlib y Seaborn (visualización estadística) y NumPy (procesamiento numérico).
