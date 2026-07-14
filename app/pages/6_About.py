import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide"
)

st.title("About")

st.markdown("""
## Student Dropout Prediction

This project was developed as the final project for the Machine Learning course.

The objective of this application is to predict whether a student is likely
to graduate or drop out using machine learning techniques.

The project includes the following stages:

- Data Understanding
- Data Preparation
- Exploratory Data Analysis
- Machine Learning Model Development
- Model Evaluation
- Model Interpretation
- Streamlit Deployment

Three classification algorithms were evaluated:
- Logistic Regression
- Decision Tree
- XGBoost

Based on the evaluation results, Logistic Regression achieved the best overall
performance and was selected as the final deployment model.
""")

st.subheader("Technologies")

st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Matplotlib
- Seaborn
- Streamlit
""")