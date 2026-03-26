# 🏦 Predicción de Suscripción a Depósito a Plazo Fijo

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completado-success?style=for-the-badge)
![Methodology](https://img.shields.io/badge/Metodología-Clasificación-orange?style=for-the-badge)

## ⚡ Accesos Rápidos

| Archivo | Descripción |
|---|---|
| 📓 **[Notebook de Análisis](./Prediccion_Depositos.ipynb)** | Código completo en Jupyter Notebook |
| 🌐 **[Reporte Web](./Prediccion_Depositos.html)** | Versión HTML para lectura fácil |
| 💾 **[Dataset (Moro et al., 2014)](./bank-additional-full.csv)** | Archivo CSV fuente (Bank Marketing Dataset) |
| 🔮 **[Simulador de Predicción](./Simulador_Depositos.html)** | Herramienta interactiva (Próximamente) |

## Resumen Ejecutivo

### ¿De qué trata este reporte?

Este reporte desarrolla un modelo de clasificación supervisada para predecir si un cliente suscribirá un depósito a plazo fijo, a partir de los datos de campañas de telemarketing de un banco portugués. El objetivo principal es estimar la probabilidad de conversión de los clientes prospecto para priorizar inteligentemente los recursos del banco (tiempo de llamadas de operadores) y optimizar las campañas de mercadotecnia. 

---

### El Dataset: Campañas de Marketing Bancario

**¿De dónde provienen los datos?**
Los datos corresponden a las distintas campañas de contactos telefónicos realizadas por una institución bancaria en Portugal entre 2008 y 2013 (etapa crítica marcada por la recesión general europea), disponibles en el UCI Machine Learning Repository.

**Características principales:**
El dataset `bank-additional-full.csv` consta de **41,188 registros** y **21 variables**.

| Categoría | Variables Ejemplos |
|---|---|
| **Perfil del cliente** | `age`, `job`, `marital`, `education`, historial crediticio (`default`, `housing`, `loan`) |
| **Contacto y campaña** | Datos del último contacto (`contact`, `month`, `day_of_week`, `duration`), y de campañas anteriores |
| **Contexto económico** | Indicadores contextuales como  `emp.var.rate`, `cons.price.idx`, `euribor3m` |
| **Variable Objetivo** | `y` (Binaria: *yes*/*no* indicando la suscripción exitosa al depósito) |

---

### Exploración Inicial y Desafíos de Datos

Al realizar un análisis exploratorio preliminar se identificaron problemáticas y consideraciones cruciales para el futuro modelado:

1. **Desbalance extremo de clases:** Existe una proporción de respuesta negativa frente a positiva de **7.9 a 1**, significando que menos del 12% del listado finalmente suscribieron al producto. Evaluar los modelos solamente en base al *accuracy* arrojaría información ilusoria. Como respuesta, este análisis se enfoca en métricas robustas ante sesgo poblacional como **AUC-ROC** y **F1-Score**.
2. **Naturaleza teórica vs práctica de las variables:** 
   - Multiples **Indicadores macroeconómicos** se publican con frecuencia mensual y trimestral, dotándolos estadísticamente de un comportamiento *cuasi-categórico* pero con interpretación analítica meramente numérica continua.
   - Existen características peculiares como `pdays`, en donde "999" está artificialmente marcado para determinar que el cliente nunca ha sido prospectado, obligando la creación de nuevas variables combinatorias.
3. **Conversión matemática de categorías (*One-Hot Encoding*):** Se adaptan atributos meramente semánticos y ordinales (como el nivel educativo o civil) a esquemas numéricos con los que los algoritmos de predicción puedan transaccionar apropiadamente.

En las secciones subsiguientes del *Notebook* se navega un riguroso recorrido a través del preprocesamiento, escalamiento comparativo y el entrenamiento hiperparametrizado contra múltiples arquitecturas algorítmicas, desde Modelos Basales, Random Forests, Suport Vector Machines, hasta Perceptrones Multicapas (Redes Neuronales).

[⬅️ Volver al Portafolio](../../README.md)
