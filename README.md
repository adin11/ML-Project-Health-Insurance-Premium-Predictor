![banner](assets/banner.png)  

# Health Rate - Your Health Insurance Premium Calculator

### App Link: [Health Rate](https://healthrate.onrender.com)

---

## 🔍 Business Problem:
Rising health insurance costs have made it difficult for individuals to estimate how much they might need to pay each year. With premiums influenced by a range of personal factors—like age, medical history, and lifestyle—many people are left guessing. In this project we will aim to solve this problem to bring clarity among individuals of differet age groups/health conditions etc.

---

## Overview:
Developed an intelligent, real-time health insurance premium predictor designed to help individuals estimate their annual premiums based on their health conditions, age, income, and more. Get Realtime Insurance estimations using this tool. Built using a Fine tuned XG-Boost Model with high accuracy.

---

## Demo
https://github.com/user-attachments/assets/17aadca1-34b6-4559-b12a-8fbe5a0c9e92

---

## Power BI Dashboard:
![dashboard](assets/dashboard.png)
**A Real-Time Dynamic Power Bi Dashboard for Analyzing How Health Insurance Premiums Differes from regions, Health,employment smoking status etc.**

--- 

## Technical Details:

### 📊 EDA
- Histograms, box plots used for univariate analysis.
- BarPlots, scatter plots and cross-tabs for bivariate insights.

### 🧠 Feature Engineering
- Created `risk_score` feature from domain-specific medical history column.
- Encoded categorical features via One-Hot encoding and Manual Label Mapping.

### 🧮 Encoding & Scaling
- Dropped multicollinear features using variance inflation factor.
- Scaled the numeric features using min/max scaling.

### 🤖 Model Development
- Trained Linear, Ridge, and XGBoost regressors.
- Finalized and Fine tuned XGBoost model using randomized search cv best R² score/test_set_score (0.98) and root mean sqaured error (1169).

### 🔀 Model Segmentation
- Identified that ~30% of predictions in younger age groups (≤ 25) had error margins exceeding 10%, leading to potential overcharging or undercharging.
- Introduced an additional feature (`genetical_risk_score`) for these groups to reduce extreme errors.
- Trained and saved two separate models for age groups ≤ 25 and > 25 using joblib.

### 🛠️ Model Tuning
- Used RandomizedSearchCV for hyperparameter optimization and trained the final model on these hyperparamters
Best Parameters:  {'n_estimators': 50, 'max_depth': 5, 'learning_rate': 0.1}

---

## 📈 Evaluation Metrics
- **R² Score (XGBoost):** 0.98  
- **Error Margin:** Minimized after age-wise segmentation.  
- **Feature Impact:** Income, risk_score, and genetical_risk were most influential features.
- **Model Strategy:** For Real Time Predictions, If the selected age is over 25, it uses one model to show results. If it's above 25 it uses a different model.

---

# Key Insights:

## 1. Age vs Premium:
![line chart](assets/age.png)


**This Line chart shows how the premium costs varies across different age groups.Younger individuals tend to pay lower insurance premiums, whereas premiums significantly increase with age.**

## 2. BMI Category Impact:
![bmigraph](assets/bmi.png)


**Insurance premiums are higher for individuals classified as Overweight or Obese, while those with a Normal or Underweight BMI enjoy lower premium rates.**

## 3. Income Level Distribution:
![incomelevel](assets/income.png)


**A majority (38%) of policyholders have an income below ₹10 lakhs. Only 16% of policy holders have income more than ₹30 lakhs.**


## 4. Employemnt Type & Insurance Plan:
![esi](assets/insure.png)

**Freelancers have the highest average income, followed by Self-Employed and then Salaried professionals. Most Gold plans are opted for by the Self-Employed, Silver by Freelancers, and Bronze by Salaried individuals.**

## 5. Premium Income Ratio [PIR]:
![medical](assets/pri.png)


**The Premium Income Ratio indicates a persons income towards their insurance premium. For age groups less than 40 PIR is less meaning the premium is more affordable, For people with more than 40 Age the PIR is High indicating higher insurance costs with respect to their income.**

## 6. Region Policy Distribution:
![esi](assets/region.png)

**The Southeast region accounts for the highest share of policies (35%), followed by Southwest (33%), Northwest (20%), and Northeast (14%).**

## 7. Smoking Habits & Premium Costs:
![esi](assets/smoke.png)

**Regular smokers pay significantly higher premiums, followed by occasional smokers. Non-smokers benefit from the lowest premium rates.**

--- 

# ⚙️ Tech Stack:
- Python (3.10+)
- Pandas, NumPy, Matplotlib, Seaborn, variance inflation factor
- Scikit-learn, XGBoost
- Streamlit (UI)
- RandomizedSearchCV (for model tuning)
- Render (Deployment) 

---


## 📌 Top Conclusions:
- Premiums are strongly influenced by medical history and income level.
- Segmented model approach significantly improved younger user predictions.
- Adding domain-specific features resulted in a more generalized model.

---
