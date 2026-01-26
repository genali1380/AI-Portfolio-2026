# 🌍 Econometric Analysis: Determinants of Global Happiness

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

## 📊 Project Description
This project presents a statistical and inferential analysis designed to answer a classic question from behavioral economics: **Does money buy happiness?**

The study begins with an initial exploration between Gross Domestic Product (GDP) and reported Happiness, then expands into a **Multiple Regression Model**. The objective is to contrast whether economic income alone is sufficient to predict a nation's well-being, or whether it loses relevance when considering more human social factors such as health, freedom, and social support.

## 📂 Data Sources
For this analysis, a data integration (Data Merging) was performed to build a robust dataset:

1.  **Base Dataset (Course):** Contains the initial cross-reference of the *Happiness Index (2022)* with *GDP (2020)*. GDP from 2020 is used to capture post-pandemic economic impact.
2.  **Extended Dataset (External Source):** The study was enriched by integrating variables from the [World Happiness Report 2022 (Kaggle)](https://worldhappiness.report/ed/2022/). This allowed adding critical dimensions such as *Healthy Life Expectancy* and *Perception of Corruption*.

## 🗂️ Navigation Index
To facilitate portfolio review, resources are available in the following formats:

* 🌐 [**Interactive Report (Web View)**](./Analysis_Report.html): **Recommended format** for smooth browser reading.
* 📓 [**Technical Notebook (Jupyter Notebook)**](./Analysis_Report.ipynb): Complete source code with methodology and statistical tests.
* 💾 [**Economic Data (CSV)**](./Felicidad_y_GDP.csv): Base file used for simple regression.
* 💾 [**Social Data (CSV)**](./World_Happiness_Report_2022.csv): Complementary file for multiple regression.

---

## 📋 Variable Dictionary
The final analysis was performed on a sample of **139 countries**. Below are the technical characteristics of the variables used:

| Variable | Computational Type | Statistical Type | Description |
| :--- | :--- | :--- | :--- |
| **Felicidad** | `Float64` | Quantitative Continuous | **Target Variable.** Score on the Cantril Ladder (0-10). |
| **GDP** | `Float64` | Quantitative Continuous | Gross Domestic Product per capita (2020 nominal values). |
| **Social Support** | `Float64` | Quantitative Continuous | National average of perceived social support. |
| **Life Expectancy** | `Float64` | Quantitative Continuous | Healthy life expectancy at birth (in years). |
| **Freedom** | `Float64` | Quantitative Continuous | Freedom index for making life decisions. |
| **Generosity** | `Float64` | Quantitative Continuous | Population's willingness to make donations. |

> ### 💡 Technical Note on Transformations
> Due to the exponential nature of the global economy, the **`GDP`** variable was subjected to a logarithmic transformation (`np.log`) within the notebook. This converts its statistical type to a linearized scale to comply with OLS regression assumptions.

---

## 🛠️ Tools Used
* **Language:** Python 3.
* **Libraries:** `Pandas` (Cleaning and Merging), `Statsmodels` (Statistical Inference), `Matplotlib` & `Seaborn` (Visualization).
* **Techniques:** Linear Regression (Simple and Multiple), Shapiro-Wilk Test, Partial F-Test.

---
*Academic project developed for the Artificial Intelligence portfolio (Universidad de Monterrey).*
