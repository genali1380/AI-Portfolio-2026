# 📊 Análisis Predictivo del Perfil del Empleador: LDA vs. Árboles de Decisión

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completado-success?style=for-the-badge)
![Methodology](https://img.shields.io/badge/Metodología-Clasificación_Supervisada-orange?style=for-the-badge)

## 📑 Resumen Ejecutivo

Este estudio aborda un problema clásico de **clasificación con clases altamente desbalanceadas** en el contexto del mercado laboral mexicano. El objetivo es predecir si un individuo ocupado es un **Empleador** o un **Empleado Subordinado**, evaluando y comparando el rendimiento de dos algoritmos de clasificación de diferente naturaleza matemática:
1. **Linear Discriminant Analysis (LDA):** Un modelo generativo basado en fronteras de decisión lineales y supuestos de normalidad.
2. **Árboles de Decisión (Decision Trees - DT):** Un modelo discriminativo no paramétrico basado en particiones ortogonales y reglas heurísticas (Criterio de Gini).

A lo largo del reporte, se explora no solo qué algoritmo tiene mejores métricas, sino *por qué* uno supera al otro debido a la naturaleza de los datos y el manejo del desbalance poblacional (93% vs 7%).

---

## ⚡ Accesos Rápidos

| Archivo | Descripción |
|---|---|
| 🌐 **[Reporte Interactivo (Vista Web)](./Reporte-Analisis.html)** | **Recomendado:** Versión HTML renderizada para lectura fluida. |
| 📓 **[Cuaderno Técnico (Notebook)](./Reporte-Analisis.ipynb)** | Código fuente completo, análisis exploratorio y entrenamiento de modelos. |
| 💾 **[Dataset (ENOE Simplificado)](./ENOE_SDEMT325_simplificado.csv)** | Dataset depurado utilizado para el análisis. |

---

## 🗂️ Fuente y Características de los Datos

Los datos provienen de la **Encuesta Nacional de Ocupación y Empleo (ENOE)** del INEGI (Tercer Trimestre de 2025). El dataset utilizado en este proyecto es un subconjunto *previamente limpiado y filtrado*, enfocado en la población económicamente activa de interés.

### Filtros Principales Aplicados:
* **Mayoría de edad:** Exclusivamente mayores de 18 años.
* **Ingresos coherentes (No ficticios):** Se incluyen únicamente registros con salarios mensuales reales reportados en el rango de **$500 a $900,000 MXN**, eliminando nulos y ceros (trabajo no remunerado).
* **Posición Ocupacional Específica:** Se excluyeron los trabajadores por "cuenta propia", manteniendo solo `pos_ocu=1` (Empleado subordinado) y `pos_ocu=2` (Empleador/Patrón).

### Diccionario de Variables (Predictores y Objetivo)

Para este análisis logístico, es fundamental entender la naturaleza estadística de cada feature:

| Variable | Tipo Estadístico | Descripción |
| :--- | :--- | :--- |
| `eda` | Numérica Discreta | Edad del trabajador (18 – 98 años). *Tratada como discreta por ser un conteo exacto de años cumplidos en la encuesta.* |
| `es_mujer` | Categórica Binaria | 1 = Mujer, 0 = Hombre. |
| `anios_esc` | Numérica Discreta | Años de escolaridad formal completados (0 – 24). |
| `log_ingocup` | Numérica Continua | Logaritmo natural del ingreso mensual ocupacional. |
| **`clase`** | **Binaria (Target)** | **1 = Empleador (Clase Minoritaria), 0 = Empleado (Clase Mayoritaria).** |

---

## 🧠 Metodología Destacada

El reporte no se limita a ejecutar código, sino que justifica rigurosamente cada decisión técnica tomada para combatir el sesgo del modelo:

1. **Evaluación de Supuestos (LDA):** Análisis de la normalidad (Shapiro-Wilk) y la homoscedasticidad (matrices de covarianza) para entender las debilidades del Análisis Discriminante Lineal ante este dataset.
2. **Mitigación del Desbalance:** 
   * Uso de probabilidades a priori iguales (`priors=[0.5, 0.5]`) en LDA.
   * Asignación de pesos balanceados (`class_weight='balanced'`) en el Árbol de Decisión.
3. **Control de Sobreajuste (Overfitting):** Implementación de **Cost Complexity Pruning (CCP)** usando Validación Cruzada (*5-Fold CV*) para encontrar el parámetro de poda ($\alpha$) óptimo en el Árbol de Decisión.
4. **Métricas de Evaluación Reales:** Abandono del *Accuracy* como métrica principal, enfocando la comparativa en **F1-Score, AUC-ROC**, y análisis directo de la **Matriz de Confusión** (Verdaderos Positivos vs. Falsos Positivos).

[⬅️ Volver al Portafolio](../../README.md)
