# 🏢 Perfil del Empleador Mexicano: Clasificación Logística

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completado-success?style=for-the-badge)
![Methodology](https://img.shields.io/badge/Metodología-Regresión_Logística-orange?style=for-the-badge)

## 📊 Descripción del Proyecto
Este estudio aplica un modelo de **Regresión Logística** para clasificar a individuos ocupados como **Empleadores** o **Empleados Subordinados** en el mercado laboral mexicano. Mediante un modelo unificado (`sm.GLM` con pesos balanceados), se obtiene tanto la inferencia econométrica (coeficientes, *p-values*) como las predicciones balanceadas en un solo marco estadístico coherente.

### Fuente de Datos
Los datos provienen de la **Encuesta Nacional de Ocupación y Empleo (ENOE)** del INEGI, correspondiente al **tercer trimestre de 2025**. La codificación de la variable `pos_ocu` se verificó directamente contra la documentación técnica oficial del INEGI.
* 🔗 **Fuente Original:** [INEGI — ENOE](https://www.inegi.org.mx/programas/enoe/15ymas/)

## 🗂️ Índice de Navegación
Para facilitar la revisión del estudio, los recursos se presentan en los siguientes formatos:

* 🌐 [**Reporte Interactivo (Vista Web)**](./A2.1_612864.html): **Formato recomendado** para lectura fluida en navegador.
* 📓 [**Cuaderno Técnico (Jupyter Notebook)**](./A2.1_612864.ipynb): Documento con código fuente y metodología para reproducibilidad.
* 💾 **[Dataset (ENOE)](https://drive.google.com/file/d/1iZ1h2U1aPbuX8et0umsLbRLgTDI60XBW/view?usp=sharing)**: Archivo CSV fuente (T3 2025).

---

## 📋 Características del Conjunto de Datos
La muestra final, tras limpieza y filtrado, se compone de **91,241 observaciones** de trabajadores ocupados mayores de 18 años con ingreso positivo, distribuidos en un **93% de empleados** y **7% de empleadores**.

### Diccionario de Variables

| Variable | Tipo | Descripción |
| :--- | :--- | :--- |
| **eda** | Numérica | Edad cronológica del trabajador (18+ años). |
| **es_mujer** | Binaria (0/1) | Indicador de género femenino, derivado de `sex`. |
| **anios_esc** | Numérica | Años de escolaridad formal completados. |
| **log_ingocup** | Numérica | Logaritmo natural del ingreso mensual por ocupación (`ingocup`). |
| **es_empleador** | Binaria (0/1) | **Variable Objetivo:** 1 = Empleador (`pos_ocu=2`), 0 = Empleado subordinado (`pos_ocu=1`). |

> ### 💡 Notas Técnicas
> 1. **Codificación INEGI verificada:** `pos_ocu=1` corresponde a "Trabajadores subordinados y remunerados" (Empleado) y `pos_ocu=2` a "Empleadores" (Patrón), según el Catálogo de Descripción de Archivos de la ENOE (Campo 58).
> 2. **Exclusión de cuenta propia:** Se excluyó `pos_ocu=3` (Trabajadores por cuenta propia) por su ambigüedad conceptual entre emprendimiento y autoempleo informal.
> 3. **Transformación logarítmica:** El ingreso se transformó a escala logarítmica para estabilizar la varianza y mejorar la linealidad. Su interpretación en el modelo se realiza mediante **elasticidades** (ver Sección 6 del reporte).

## 🛠️ Herramientas Utilizadas
* **Lenguaje:** Python 3.14
* **Procesamiento:** `Pandas`, `NumPy`.
* **Modelado:** `Statsmodels` (GLM Binomial con `var_weights`), `Scikit-Learn` (CV, métricas).
* **Visualización:** `Seaborn` y `Matplotlib`.
