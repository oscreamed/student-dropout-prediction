# Student Dropout Prediction System

## Overview

Student Dropout Prediction System is a Machine Learning application developed to predict whether a student is likely to **Graduate** or **Dropout** based on academic, demographic, and socio-economic factors.

The project compares multiple classification algorithms and deploys the best-performing model using Streamlit.

---

## Objectives

- Analyze factors related to student dropout.
- Compare multiple machine learning classification algorithms.
- Select the best-performing model.
- Interpret the prediction results.
- Deploy the final model as an interactive web application.

---

## Dataset

The dataset contains student information such as:

- Age
- Gender
- Family Income
- Internet Access
- Study Hours per Day
- Attendance Rate
- Assignment Delay Days
- Travel Time Minutes
- Part-Time Job
- Scholarship
- Stress Index
- GPA
- Semester GPA
- CGPA
- Semester
- Department
- Parental Education

Target Variable:

- Graduate (0)
- Dropout (1)

---

## Machine Learning Workflow

1. Data Understanding
2. Data Preparation
3. Exploratory Data Analysis
4. Model Development
5. Hyperparameter Tuning
6. Model Evaluation
7. Model Interpretation
8. Deployment

---

## Models Evaluated

- Logistic Regression
- Decision Tree
- XGBoost

### Best Model

**Logistic Regression**

Performance on the test set:

| Metric | Score |
|--------|--------:|
| Accuracy | 79.80% |
| Precision | 0.62 |
| Recall | 0.35 |
| F1-Score | 0.45 |

---

## Model Interpretation

Feature interpretation was performed using:

- Feature Importance
- SHAP (SHapley Additive exPlanations)

The analysis shows that academic performance is the strongest predictor of student graduation status. GPA is the most influential feature, followed by Stress Index, Attendance Rate, Semester GPA, and Travel Time Minutes.

---

## Deployment

The final model was deployed using **Streamlit**.

The application allows users to:

- Explore the dataset
- View model evaluation results
- Interpret feature importance
- Predict student graduation status interactively

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
- Streamlit

---

## Project Structure

```
student-dropout-prediction/
│
├── app/
│   ├── app.py
│   ├── assets/
│   └── pages/
│
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

## Installation

Clone the repository:

```bash
git clone https://github.com/oscreamed/student-dropout-prediction.git
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

## Live Demo

Streamlit App:

https://student-dropout-prediction-by-oza.streamlit.app

GitHub Repository:

https://github.com/oscreamed/student-dropout-prediction

---

## Author

**Oryza Sekar Rismadhani**

Bachelor of Informatics Engineering  
Universitas Dian Nuswantoro

Machine Learning Final Project (2025/2026)