# 🏥 Medical Cost Intelligence System


![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

> An end-to-end **Machine Learning and Analytics Dashboard** that predicts healthcare insurance costs using demographic and health data.

---

# 📌 Project Overview

Healthcare insurance companies must estimate medical costs accurately in order to:

- Set fair premium pricing
- Reduce financial risk
- Identify high-risk customers
- Improve profitability

This project builds a **Machine Learning system** that predicts **individual medical insurance charges** and provides **interactive analytics using Streamlit**.

The solution includes:

- Exploratory Data Analysis (EDA)
- Machine Learning model comparison
- Model evaluation
- Real-time prediction system
- Interactive analytics dashboard

---

# 🎯 Business Objective

To build a predictive analytics system that helps insurance companies:

- Estimate medical insurance costs
- Identify high-risk individuals
- Support risk-based pricing strategies
- Enable data-driven decision making

---

# 📊 Dataset Information

**Dataset:** Medical Insurance Dataset  

| Feature | Description |
|-------|-------------|
| age | Age of the individual |
| sex | Gender |
| bmi | Body Mass Index |
| children | Number of dependents |
| smoker | Smoking status |
| region | Residential region |
| charges | Medical insurance cost (Target Variable) |

**Dataset Size**

- Records: **1338**
- Features: **6 input variables + 1 target**

---

# 🔎 Exploratory Data Analysis

EDA was performed to understand patterns and cost-driving factors.

### Key Insights

- **Smoking status has the highest impact on medical charges**
- **Age shows moderate positive correlation with cost**
- **BMI contributes to increasing healthcare expenses**
- **Number of children has minimal impact**

### Visualizations Included

- Univariate Analysis
- Bivariate Analysis
- Multivariate Correlation Heatmap

---

# 🤖 Machine Learning Models Used

The following regression models were trained and compared:

1. Linear Regression
2. K-Nearest Neighbors (KNN)
3. Support Vector Machine (SVM)
4. Decision Tree Regressor
5. Random Forest Regressor

---

# 🏆 Final Model Selection

**Random Forest Regressor**

Reasons for selecting Random Forest:

- Handles **non-linear relationships**
- Captures **feature interactions**
- Reduces **overfitting through ensemble learning**

---

# 📈 Model Performance

Evaluation metrics used:

- **Mean Absolute Error (MAE)**
- **R² Score**

### Best Model Result

| Model | R² Score | MAE |
|------|------|------|
| Random Forest | **~0.85** | Lowest |

The model explains **approximately 85% of variance in medical charges**.

---

# 🖥️ Streamlit Dashboard

The project includes an interactive **Streamlit application** with two modules.

## 📊 Analytics Dashboard

- Key KPI metrics
- Univariate analysis
- Bivariate analysis
- Correlation heatmap

## 💰 Prediction Engine

Users can input:

- Age
- Gender
- BMI
- Number of children
- Smoking status
- Region

The system predicts **estimated medical insurance cost instantly**.

---




---

# 🛠️ Tech Stack

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit
- Joblib
---
### Tools

- Jupyter Notebook
- VS Code
- GitHub

---

# 📂 Project Structure
Medical_Cost_Intelligence_system  
│  
├── app.py  
├── insurance.csv  
├── best_model.pkl  
├── EDA.ipynb  
└── README.md  
---

# Dashboard Preview
images/dashboard.png
images/prediction.png
