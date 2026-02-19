# 📊 Análisis de Determinantes del Ingreso en México

## ⚡ Accesos Rápidos

| Archivo | Descripción |
|---|---|
| 📓 **[Notebook de Análisis](./Analisis_Ingresos.ipynb)** | Código completo en Jupyter Notebook |
| 🌐 **[Reporte Web](./Analisis_Ingresos.html)** | Versión HTML para lectura fácil |
| 💾 **[Dataset (ENOE)](https://drive.google.com/file/d/1iZ1h2U1aPbuX8et0umsLbRLgTDI60XBW/view?usp=sharing)** | Archivo CSV fuente (T3 2025) |

## Resumen Ejecutivo

### ¿De qué trata este reporte?

Este reporte construye un modelo estadístico para cuantificar qué factores determinan el ingreso mensual de los trabajadores en México, y en qué magnitud. No se limita a describir quién gana más — busca medir *cuánto* vale cada variable de forma aislada, controlando por el resto.

---

### El Dataset: ENOE 2025

**¿Qué es la ENOE?**
La Encuesta Nacional de Ocupación y Empleo es el instrumento oficial del INEGI para medir el mercado laboral mexicano. Se aplica trimestralmente a hogares de todo el país con metodología estandarizada y cobertura nacional, lo que la convierte en la fuente de referencia para cualquier análisis serio sobre ingresos en México.

**¿Qué edición se usó?**
Tercer Trimestre de 2025 (`ENOE_SDEMT325.csv`).

**¿Qué variables se extrajeron?**

| Variable | Descripción |
|---|---|
| `eda` | Edad del trabajador |
| `sex` | Género (1=Hombre, 2=Mujer) |
| `anios_esc` | Años de escolaridad completados |
| `pos_ocu` | Posición ocupacional (1=Patrón, 2=Cuenta propia, 3=Empleado) |
| `ingocup` | Ingreso mensual por ocupación en pesos MXN — **variable objetivo** |
| `hrsocup` | Horas trabajadas por semana |

---

### Exploración y Limpieza de Datos

El dataset crudo contenía **+400,000 registros** tras aplicar el filtro de mayoría de edad (≥18 años). Sin embargo, no todos eran utilizables para el análisis. El proceso de limpieza operó en varias capas:

**1. Filtros lógicos y biológicos:**
- Se eliminaron menores de 18 años (fuera del mercado laboral formal).
- Se descartaron trabajadores con más de 30 años de escolaridad (implausible) o con más años de escuela que de edad menos 3 (imposible cronológicamente).
- Se filtraron jornadas fuera del rango humano: menos de 10 o más de 100 horas semanales.

**2. Filtro de ingresos:**
- Se aplicó un rango de **$500 a $900,000 MXN mensuales**, con base en:
  - El límite inferior ancla al Salario Mínimo General vigente ($278.8 MXN/día en T3 2025): un ingreso menor a $500 implica menos de 2 días trabajados al mínimo, lo cual es incoherente con la definición de "ocupado" de la ENOE.
  - El límite superior corresponde al percentil 99.99% de la distribución. La ENOE es una encuesta de hogares de propósito general, no diseñada para capturar con precisión los ingresos de la élite económica.
  - Este rango captura el **99.8% de la masa distribucional real**.

**3. Codificación de valores ausentes:**
- La ENOE usa códigos especiales (como `99999`) para ingresos desconocidos y `0` para trabajo sin pago. Estos se convirtieron a `NaN` antes de cualquier análisis.

**4. Detección de anomalías multivariable:**
- Se aplicó **Isolation Forest** sobre la muestra depurada, eliminando 750 registros adicionales cuyo perfil combinado (ingreso + horas + educación + rol) resultaba estadísticamente incoherente, aunque cada variable individual estuviera dentro de rango.

**Resultado final por etapa:**

| Etapa | Registros |
|---|---|
| Dataset crudo (≥18 años) | 303,972 |
| Tras filtros lógicos y de ingreso | ~103,541 |
| Tras Isolation Forest (población Gold) | ~14,250 |

---

### Ingeniería de Variables

Las variables originales de la ENOE no entran directamente al modelo — requieren transformación:

- **`log_ingocup`:** El ingreso se transforma con logaritmo natural. Esto corrige la distribución sesgada a la derecha típica de los salarios y permite interpretar los coeficientes directamente como variaciones porcentuales.
- **`log_hrsocup`:** Igual tratamiento para las horas, lo que permite estimar una *elasticidad* (variación porcentual del ingreso ante variación porcentual de las horas).
- **`experiencia`:** En lugar de usar la edad cruda, se calcula la **Experiencia Potencial de Mincer**: `Edad − Escolaridad − 6`. Esto representa los años efectivos disponibles para haber trabajado.
- **`exp_cuadrado`:** El cuadrado de la experiencia captura los rendimientos decrecientes — la experiencia aporta cada vez menos ingreso conforme avanza.
- **`es_mujer`:** Variable binaria derivada de `sex`.
- **Dummies de rol:** `rol_patron`, `rol_cuenta_propia` (referencia: empleado asalariado).

---

### Hallazgos Principales

Con 103,541 observaciones y errores estándar robustos (HC1):

| Factor | Impacto sobre el ingreso |
|---|---|
| Cada año de escolaridad | **+6.21%** |
| Ser mujer | **−18.54%** |
| Ser patrón (vs. empleado) | **+26.03%** |
| Ser cuenta propia (vs. empleado) | **+57.51%** |
| Pico salarial por experiencia | A los **33.3 años** de trayectoria |

El modelo con mejor desempeño predictivo (R²=0.3728 en test set) fue entrenado sobre la población depurada con Isolation Forest (14,250 registros). El R² de ~0.33 en la muestra completa es consistente con el rango esperado en econometría de comportamiento humano (0.10–0.40).

[⬅️ Volver al Portafolio](../../README.md)
