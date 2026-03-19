# 🚀 Predicción de Roles Laborales: Modelos de Ensamble, SVM y Redes Neuronales

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completado-success?style=for-the-badge)
![Methodology](https://img.shields.io/badge/Metodología-Aprendizaje_No_Lineal-orange?style=for-the-badge)

## 📑 Resumen Ejecutivo

Este estudio representa la fase más avanzada del análisis predictivo sobre el mercado laboral mexicano. Tras haber evaluado modelos lineales y árboles de decisión simples, este reporte se enfoca en la implementación coordinada y comparativa de cuatro algoritmos de alta complejidad:
1. **Random Forest (Bagging):** Construcción de múltiples árboles independientes para reducir la varianza.
2. **AdaBoost (Boosting):** Entrenamiento secuencial enfocado en la corrección de errores de instancias difíciles.
3. **Support Vector Machines (SVM):** Búsqueda de un hiperplano de margen máximo utilizando un kernel RBF para capturar relaciones no lineales.
4. **Redes Neuronales (MLP):** Un perceptrón multicapa diseñado con una arquitectura parsimoniosa para evitar el sobreajuste.

El objetivo central es determinar si el aumento en la complejidad arquitectónica de los modelos se traduce en una mejora significativa en la detección de la clase minoritaria (**Empleadores**) en un entorno de datos tabulares con un desbalance de 13.4:1.

---

## ⚡ Accesos Rápidos

| Archivos | Descripción |
|---|---|
| 🌐 **[Reporte Interactivo (Vista Web)](./Reporte-Analisis.html)** | **Recomendado:** Lectura fluida con visualizaciones renderizadas. |
| 📓 **[Cuaderno Técnico (Notebook)](./Reporte-Analisis.ipynb)** | Código fuente, hiperparámetros y flujo de entrenamiento completo. |
| 💾 **[Dataset (ENOE Simplificado)](./ENOE_SDEMT325_simplificado.csv)** | Conjunto de datos depurado con ~91k registros. |

---

## 🗂️ Fuente y Características de los Datos

Los datos provienen de la **Encuesta Nacional de Ocupación y Empleo (ENOE)** del INEGI (T3 2025). La muestra ha sido filtrada para incluir únicamente a trabajadores mayores de edad con ingresos reales reportados.

### Diccionario de Variables

| Variable | Tipo Estadístico | Descripción |
| :--- | :--- | :--- |
| `eda` | Numérica Discreta | Edad del trabajador (18 – 98 años). |
| `es_mujer` | Categórica Binaria | 1 = Mujer, 0 = Hombre. |
| `anios_esc` | Numérica Discreta | Años de escolaridad formal completados. |
| `log_ingocup` | Numérica Continua | Logaritmo natural del ingreso mensual ocupacional. |
| **`es_empleador`** | **Binaria (Target)** | **1 = Empleador, 0 = Empleado.** |

> ### 💡 Nota sobre la variable `eda`
> Estadísticamente, la variable `eda` se trata como **numérica discreta**, ya que en la encuesta se reportan únicamente años cumplidos (números enteros), sin fracciones decimales de tiempo. No obstante, para fines de modelado en SVM y Redes Neuronales, es estandarizada para facilitar el cálculo de gradientes y distancias.

---

## 🧠 Metodología Destacada

- **Compensación de Desbalance:** Se utilizaron técnicas de `class_weight='balanced'` en RF y SVM, y pesos de muestra (`sample_weight`) calculados manualmente para AdaBoost y MLP.
- **Escalamiento Riguroso:** Implementación de `StandardScaler` con ajuste exclusivo en el set de entrenamiento para prevenir *data leakage*.
- **Métricas Críticas:** Evaluación centrada en **F1-Score** y **AUC-ROC** para ignorar el sesgo de la precisión (Accuracy) engañosa.

[⬅️ Volver al Portafolio](../../README.md)
