import streamlit as st

st.set_page_config(
    page_title="Student Dropout Prediction",
    layout="wide"
)

st.title("Student Dropout Prediction System")

st.markdown("""
Welcome to the **Student Dropout Prediction System**.

This application was developed to predict whether a student is likely to **Graduate** or **Dropout** using a Machine Learning model.

The best-performing model selected in this project is **XGBoost**, trained and evaluated using various classification metrics and interpreted using **SHAP (SHapley Additive exPlanations)**.
""")

st.divider()

# =====================================================
# Project Objective
# =====================================================

st.header("Project Objective")

st.write("""
The objective of this project is to identify students who are at risk of dropping out as early as possible.

Early prediction enables universities to provide appropriate academic support and interventions, helping improve student retention and graduation rates.
""")

# =====================================================
# Workflow
# =====================================================

st.divider()

st.header("⚙️ Machine Learning Workflow")

st.markdown("""
1. Data Understanding
2. Data Preparation
3. Model Training
4. Hyperparameter Tuning
5. Model Evaluation
6. Model Interpretation using SHAP
7. Deployment with Streamlit
""")

# =====================================================
# Technologies
# =====================================================

st.divider()

st.header("🛠 Technologies")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
**Programming Language**
- Python

**Machine Learning**
- XGBoost
- Scikit-learn

**Model Interpretation**
- SHAP
""")

with col2:
    st.markdown("""
**Data Processing**
- Pandas
- NumPy

**Visualization**
- Matplotlib
- Seaborn
- Plotly

**Deployment**
- Streamlit
""")

# =====================================================
# Navigation
# =====================================================

st.divider()

st.header("Application Pages")

st.info("""
Use the navigation menu on the left to explore each section of the application.

- Dashboard
- Exploratory Data Analysis (EDA)
- Prediction
- Evaluation
- Interpretation
- About
""")

# =====================================================
# Footer
# =====================================================

st.divider()

st.caption("Machine Learning Final Project | Student Dropout Prediction using XGBoost")