# 🧬 Subtipos Moleculares en HNSC: Análisis Transcriptómico

## ⚡ Accesos Rápidos

| Archivo | Descripción |
|---|---|
| 📓 **[Notebook de Análisis](./Analisis_TCGA_HNSC.ipynb)** | Código completo en Jupyter Notebook |
| 🌐 **[Reporte Web](./Analisis_TCGA_HNSC.html)** | Versión HTML para lectura fácil |
| 📊 **[Presentación Interactiva](./presentacion_HNSC.html)** | Diapositivas dinámicas con visualizaciones de resultados |
| 💾 **[Dataset (TCGA-HNSC) - Expresión y Fenotipos](https://drive.google.com/drive/folders/1HuqybgWr0UlsQYgotS_BhIC6HDQbdHfG?usp=sharing)** | Archivos crudos alojados externamente por tamaño (Drive) |

## Resumen Ejecutivo

### ¿De qué trata este reporte?

Este proyecto emplea técnicas de **aprendizaje automático no supervisado** para analizar la expresión génica (transcriptoma) de más de 500 pacientes con Carcinoma de Células Escamosas de Cabeza y Cuello (HNSC). El objetivo es descubrir estructuras biológicas subyacentes y subtipos moleculares que determinan la agresividad de la enfermedad, y que no son evidentes mediante clasificaciones clínicas convencionales.

---

### El Dataset: TCGA-HNSC

**¿Qué es el TCGA?**
The Cancer Genome Atlas (TCGA) es uno de los repositorios multiómicos públicos más grandes de la historia, diseñado para caracterizar molecularmente miles de tumores y avanzar en el campo de la oncología.

**¿Qué datos se utilizaron en este proyecto?**
- Datos de expresión génica cuantificados en Transcritos por Millón (TPM) para más de 60,000 entidades.
- Metadatos fenotípicos y clínicos de los pacientes (edad, género, estadío tumoral, historial tabáquico en cajetillas-año, estado vital, etc.).

---

### Metodología de Procesamiento y Análisis

El transcriptoma nativo presentaba más de 60,000 características moleculares por paciente, lo que introduce el problema matemático de la *"maldición de la dimensionalidad"*. El pipeline metodológico aplicado para superarlo fue:

**1. Limpieza y Normalización:**
- Remoción de valores atípicos severos detectados mediante algoritmos multivariantes.
- Transformación logarítmica (Log2) para estabilizar la sobredispersión, típica en datos de secuenciación masiva (Bulk RNA-Seq).

**2. Selección de Variables (Filtrado de Varianza):**
- Uso del estimador robusto **MAD (Desviación Absoluta Mediana)** para priorizar genes con varianza biológicamente relevante, extrayendo los 5,000 genes más informativos y aislando el ruido estocástico del fondo.

**3. Reducción Dimensional:**
- Proyección lineal mediante el **Análisis de Componentes Principales (PCA)**, logrando condensar matemáticamente el 90% de la varianza tumoral en un espacio latente de 219 componentes.

**4. Agrupamiento No Supervisado:**
- Evaluación comparativa entre **K-Means** y **Clustering Jerárquico** (enlace de Ward).
- Optimización rigurosa usando los coeficientes de **Silhouette** y **Davies-Bouldin**, identificando $K=2$ como la segmentación estructural primaria de la cohorte.

---

### Hallazgos Clínicos y Oncológicos

El algoritmo no supervisado descubrió —de forma completamente "ciega"— dos perfiles transcriptómicos diametralmente opuestos. Más del 82.8% del genoma filtrado se expresó diferencialmente entre los grupos. Estas particiones **no** correlacionaron con las variables clínicas clásicas (como edad, género o estadío patológico), pero lograron separar exitosamente la etiología subyacente y la respuesta al tratamiento:

| Subtipo Molecular | Etiología Dominante | Sitio Anatómico | Propensión Invasiva Temprana | Supervivencia a Largo Plazo |
|---|---|---|---|---|
| **Cluster 0** | **VPH** (Papiloma) | Orofaringe / Amígdalas | **Alta** metástasis ganglionar (65.7% N1-N3) | **Mayor sobrevida** (buena respuesta terapéutica) |
| **Cluster 1** | Mutagénesis por **Tabaco** | Cavidad Oral / Laringe | **Menor** metástasis inicial (51.6% N1-N3) | **Peor pronóstico** (resistencia terapéutica) |

### Conclusión
El modelo capturó matemáticamente la dualidad etiológica (VPH vs. Tabaquismo) del cáncer de cabeza y cuello sin haber recibido ninguna etiqueta clínica previa. Estos hallazgos demuestran el poder del machine learning en la subtipificación genómica, aportando evidencia crucial a favor de la **medicina de precisión oncológica**, donde los tratamientos se decidan por el perfil transcriptómico del tumor individual.

---

[⬅️ Volver al Portafolio](../../README.md)
