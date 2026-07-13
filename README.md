# Student Dropout Prediction System

## Project Overview

Student Dropout Prediction System is a Machine Learning application developed to predict whether a student is likely to **Graduate** or **Dropout** based on academic and socio-economic factors.

This project applies supervised machine learning techniques to support early identification of students at risk, enabling educational institutions to provide timely academic interventions.

---

## Project Objectives

- Analyze factors influencing student dropout.
- Compare multiple classification algorithms.
- Select the best-performing model.
- Interpret model predictions using SHAP.
- Deploy the final model using Streamlit.

---

## Dataset

The dataset contains student demographic, academic, and socio-economic information, including:

- Age
- Gender
- Family Income
- Internet Access
- Study Hours
- Attendance Rate
- GPA
- Semester GPA
- CGPA
- Scholarship
- Department
- Stress Index
- Travel Time
- Parental Education

Target Variable:

- Graduate
- Dropout

---

## Project Structure

```text
student-dropout-prediction/
│
├── app/
├── data/
├── models/
├── notebooks/
├── reports/
├── src/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Machine Learning Workflow

1. Data Understanding
2. Data Preparation
3. Feature Engineering
4. Model Training
5. Hyperparameter Tuning
6. Model Evaluation
7. Model Interpretation
8. Deployment

---

## Machine Learning Models

The following models were evaluated:

- Logistic Regression
- Decision Tree
- XGBoost

### Final Model

**XGBoost**

Performance:

| Metric | Score |
|--------|--------|
| Accuracy | 79.60% |
| Precision | 0.63 |
| Recall | 0.31 |
| F1-Score | 0.42 |

---

## Model Interpretation

Model interpretation was performed using:

- Feature Importance
- SHAP Summary Plot

The most influential features include:

- GPA
- CGPA
- Attendance Rate
- Study Hours per Day

---

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Matplotlib
- Seaborn
- Plotly
- Streamlit

---

## Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/student-dropout-prediction.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app/app.py
```

---

## Author

Machine Learning Final Project

Student Dropout Prediction System
