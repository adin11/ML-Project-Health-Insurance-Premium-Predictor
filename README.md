![banner](assets/banner.png)  
Banner [source](https://banner.godori.dev/)

![Python version](https://img.shields.io/badge/Python%20version-3.10%2B-lightgrey)
![GitHub last commit](https://img.shields.io/github/last-commit/adin11/ml-project-health-premium-prediction)
![Type of ML](https://img.shields.io/badge/Type%20of%20ML-Regression-blue)
![License](https://img.shields.io/badge/License-MIT-green)
[![Streamlit App](https://img.shields.io/badge/Deployed%20with-render-purple)]()
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

# Health Insurance Premium Calculator:

### App Link: (https://healthrate.onrender.com)
### Power BI Dasboard Link: (https://app.powerbi.onrender.com)

---

## Overview:
An intelligent, real-time health insurance premium predictor designed to help individuals estimate their annual premiums based on their health conditions, age, income, and more. Get Realtime Insurance estimations using this project.

---

## 🔍 Business Problem:
Rising health insurance costs have made it difficult for individuals to estimate how much they might need to pay each year. With premiums influenced by a range of personal factors—like age, medical history, and lifestyle—many people are left guessing. This project aims to bring clarity by offering a simple, data-driven tool that helps users understand what goes into their health insurance costs and what to expect financially.

---

## Power BI Dashboard:
![dashboard](assets/dashboard.png)
**A Real-Time Dynamic Power Bi Dashboard for Analyzing How Health Insurance Premiums Differes from regions, Health,employment somking status etc.**

--- 

## Key Insights:

### 1. Age Column :
![line chart](assets/age.png)

** **

### 2. BMI Column :
![bmigraph](assets/bmi.png)

** **

### 3. Income Level :
![incomelevel](assets/income.png)
** **

### 4. Employemnt status and insurance plan :
![esi](assets/insure.png)
** **

### 5. Premium Income Ratio :
![medical](assets/pri.png)
** **

### 6. Region :
![esi](assets/region.png)
** **

### 7. Smoking Status :
![esi](assets/smoke.png)
** **

--- 

## ⚙️ Tech Stack:
- Python (3.10+)
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn, XGBoost
- Streamlit (for UI & deployment)
- RandomizedSearchCV (for model tuning)

---

## 🧪 Methods:

### 📥 Data Preprocessing
- Cleaned dataset and isolated `X` and `y` to avoid leakage.
- Applied pipelines independently to test/train splits.

### 📊 EDA
- Histograms, box plots used for univariate analysis.
- Scatter plots and cross-tabs for bivariate insights.

### 🧠 Feature Engineering
- Created `risk_score` from domain-specific medical history.
- Encoded categorical features via One-Hot and Label Mapping.

### 🧮 Feature Selection & Scaling
- Dropped multicollinear features using VIF.
- Applied Min-Max scaling for consistent range.

### 🤖 Model Development
- Trained Linear, Ridge, and XGBoost regressors.
- XGBoost selected for best R² performance (0.98).

### 🛠️ Model Tuning & Segmentation
- Used RandomizedSearchCV for hyperparameter optimization.
- Built two models: one for ≤25, one for >25 age group.

---

## 📈 Evaluation Metrics
- **R² Score (XGBoost):** 0.98  
- **Error Margin:** Minimized after age-wise segmentation  
- **Feature Impact:** Income, risk_score, and genetical_risk were most influential  
- **Model Strategy:** Balanced simplicity with high accuracy for real-world usability

---

## 📌 Key Findings:
- Premiums are strongly influenced by medical history and income level.
- Segmented model approach significantly improved younger user predictions.
- Added domain-specific features resulted in more robust generalization.

---
> 🚀 **Final solution: A dual-model XGBoost system optimized for different age groups, served through an interactive and responsive Streamlit app.**
=======

