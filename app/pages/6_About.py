import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide"
)

st.title("About")

st.write("""
This application was developed as the final project for the Machine Learning course.
""")

st.divider()

st.header("Project Overview")

st.write("""
The objective of this project is to predict whether a student is likely to Graduate or Dropout using machine learning techniques.
""")

st.divider()

st.header("Dataset")

st.write("""
The dataset contains academic and socio-economic information related to student performance and graduation status.
""")

st.divider()

st.header("Methodology")

st.markdown("""
- Data Understanding
- Data Preparation
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- SHAP Interpretation
- Streamlit Deployment
""")

st.divider()

st.header("Technologies")

st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Streamlit
- Matplotlib
- Seaborn
""")

st.divider()

st.header("Developer")

st.write("""
Machine Learning Final Project

Student Dropout Prediction using XGBoost
""")