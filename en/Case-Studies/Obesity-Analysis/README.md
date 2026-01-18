# Multidimensional Study on Obesity Risk Factors in Latin America

## 📊 Project Description
This project presents a statistical and inferential analysis of data collected from populations in **Mexico, Peru, and Colombia**. The main objective is to identify lifestyle patterns and demographic factors that have a direct correlation with obesity levels, providing a data-driven vision of this public health challenge.

The database used is a simplified version of the original dataset from the UCI Machine Learning Repository; the original dataset can be found at the following link: https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition

## 🗂️ Navigation Index
To facilitate review, the repository is structured as follows:
* 📓 [**Technical Analysis & Methodology**](./Analysis_Report.ipynb): Detailed notebook with data processing and visualizations.
* 💾 [**Original Dataset**](./Obesity_Data.csv): Source database with records of 2,111 individuals.

## 📋 Dataset Characteristics
The database consists of information collected from 2,111 individuals, capturing a diverse mix of physical profiles and behavioral habits.

### Structure and Scope
* **Volume:** 2,111 records with 10 variables each.
* **Origin:** Multicentric study conducted in Mexico, Peru, and Colombia.
* **Nature of Data:** The dataset combines numerical variables (physical measurements) and categorical variables (habits and descriptive labels).

### Variable Dictionary

| Variable | Type | Description |
| :--- | :--- | :--- |
| **Gender** | Categorical | Biological gender of the participant. |
| **Age** | Numerical | Chronological age (observed range 14 to 61 years). |
| **Height** | Numerical | Height in meters. |
| **Weight** | Numerical | Body mass in kilograms. |
| **FamilyHistoryOverweight** | Categorical | Direct family history of obesity. |
| **HighCaloricFood** | Categorical | Frequent consumption of high-calorie foods. |
| **VegetableConsumption** | Numerical | Reported frequency of vegetable consumption. |
| **Smoker** | Categorical | Identifies if the individual has a smoking habit. |
| **WaterConsumption** | Numerical | Daily water intake. |
| **ObesityLevel** | Categorical | **Target Variable:** Classification based on BMI. |

> ### 💡 Technical Note on Variables
> The variables **`VegetableConsumption`** and **`WaterConsumption`** appear in this dataset as continuous numerical values (with decimals). It is essential to clarify that, in the original study design, these represent frequency levels on a scale from **1 to 3**. The continuous nature of these values results from data preprocessing and augmentation techniques (such as SMOTE) used to balance the dataset; therefore, they should be interpreted as ordinal indicators within those levels.

## 🛠️ Tools Used
* **Language:** Python 3.14.2
* **Libraries:** Pandas (data handling), Matplotlib and Seaborn (statistical visualization), and NumPy (numerical processing).
