# 📂 Portafolio de Inteligencia Artificial | Español

Bienvenido a la sección en español de mi portafolio profesional de Inteligencia Artificial. En este apartado presento proyectos aplicados que demuestran el análisis de datos desde una perspectiva técnica, científica y estratégica.

---

## 🗂️ Índice de Casos de Estudio

### [📊 Análisis de Factores de Riesgo en Obesidad](./Estudio-de-casos/Obesity-Analysis/README.md)
**Tecnologías:** `Python`, `Pandas`, `Matplotlib`, `Seaborn`

**Resumen del reporte:**
Este estudio inferencial analiza una población de **2,111 individuos** en México, Perú y Colombia. El proyecto se centra en:
* Identificar patrones de correlación entre hábitos de vida (consumo de vegetales, actividad física) y categorías de salud.
* Validar la consistencia de los datos mediante visualizaciones avanzadas.
* Proponer mejoras en el diseño experimental mediante la inclusión de variables de gasto calórico acumulado.

---

### [📊 Análisis de Felicidad Mundial](./Estudio-de-casos/Felicidad-Analsis/README.md)
**Tecnologías:** `Python`, `Pandas`, `Matplotlib`, `Seaborn`, `Statsmodels`

**Resumen del reporte:**
Este estudio estadístico explora la relación entre el PIB y la felicidad nacional utilizando datos de **más de 140 países**. El proyecto se centra en:
* Cuantificar el impacto del ingreso económico en la felicidad mediante Regresión Lineal Simple.
* Integrar variables psicosociales (Apoyo Social, Esperanza de Vida, Libertad) mediante Regresión Lineal Múltiple.
* Probar la hipótesis de redundancia del PIB al controlar por factores de bienestar humano.

---

### [📊 Modelo Predictivo de Rendimiento Académico](./Estudio-de-casos/Calificaciones-Analisis/README.md)
**Tecnologías:** `Python`, `Pandas`, `Matplotlib`, `Seaborn`, `Statsmodels`

**Resumen del reporte:**
Este proyecto de ingeniería de datos desarrolla un modelo de regresión lineal robusto para predecir la calificación final ($G3$) de estudiantes de nivel secundaria. El análisis se centra en:
* Aplicar el **Principio de Parsimonia**, demostrando que un modelo simplificado de **3 variables** iguala la precisión de modelos complejos.
* Implementar algoritmos de selección de características (*Forward Selection*) y validación cruzada para evitar el sobreajuste.
* Gestionar casos de **deserción escolar** (ceros estructurales) para garantizar predicciones realistas y honestas.

---

### [📊 Perfil del Empleador Mexicano: Clasificación Logística](./Estudio-de-casos/Perfil-Empleador-Analisis/README.md)
**Tecnologías:** `Python`, `Pandas`, `Statsmodels`, `Scikit-learn`

**Resumen del reporte:**
Este estudio aplica **Regresión Logística** para clasificar a trabajadores como empleadores o empleados subordinados usando datos de la **ENOE 2025** (~91k observaciones). El análisis se centra en:
* Abordar el desbalance severo (93/7) mediante un modelo unificado con **pesos balanceados** (`sm.GLM` + `var_weights`).
* Cuantificar la **brecha de género patronal** (-43.5% en probabilidades para mujeres) y la relación inversa entre educación formal y emprendimiento.
* Interpretar la elasticidad logarítmica del ingreso como predictor dominante (+50.5% al duplicar ingresos).

---

### [📊 Análisis Predictivo del Perfil del Empleador: LDA vs. Árboles de Decisión](./Estudio-de-casos/LDA-y-DT.analisis/README.md)
**Tecnologías:** `Python`, `Pandas`, `Matplotlib`, `Seaborn`, `Scikit-learn`

**Resumen del reporte:**
Este estudio compara algoritmos de discriminación paramétrica (**LDA**) y particionamiento no paramétrico (**Decision Trees**) para clasificar el rol laboral frente a un desbalance severo (93/7). El análisis se centra en:
* Evaluar violaciones a la homoscedasticidad y preprocesamiento de características dependientes.
* Controlar el sesgo mayoritario mediante `priors` y de `class_weight='balanced'`.
* Detener el memorizado extremo del árbol mediante **Cost Complexity Pruning** con Validación Cruzada (F1-Score).

---

## 🗂️ Proyecto

### [📊 Análisis de Determinantes del Ingreso en México](./Proyectos/P1/README.md)
**Tecnologías:** `Python`, `Pandas`, `Statsmodels`, `Scikit-learn`

**Resumen del reporte:**
Este proyecto econométrico cuantifica los factores que determinan el ingreso laboral en México utilizando datos de la **ENOE 2025**. El análisis se centra en:
*   Estimar a través de la **Ecuación de Mincer** el retorno de la educación (+6.21% por año) y la experiencia.
*   Medir la brecha salarial de género, encontrando una penalización del **-18.54% para mujeres** *ceteris paribus*.
*   Aplicar limpieza avanzada de datos con **Isolation Forest** para eliminar anomalías multidimensionales en el mercado laboral.


[⬅️ Volver al Inicio del Portafolio](../README.md)
