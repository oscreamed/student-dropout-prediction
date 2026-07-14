import streamlit as st

st.set_page_config(
    page_title="Student Dropout Prediction",
    layout="wide"
)

st.title("Student Dropout Prediction")

st.divider()

st.markdown("""
Welcome to the **Student Dropout Prediction** application.

This application predicts whether a student is likely to **Graduate** or **Dropout**
using a **Logistic Regression** machine learning model.

The prediction is based on various academic and socio-economic factors such as academic performance,
attendance, study habits, financial background, and other student-related attributes.

Use the navigation menu on the left to explore the dataset, perform exploratory data analysis,
generate predictions, evaluate the model, and understand the factors influencing the prediction results.
""")

st.divider()

st.subheader("Application Pages")

st.markdown("""
- **Dashboard** – Overview of the dataset.
- **EDA** – Exploratory Data Analysis.
- **Prediction** – Predict student graduation or dropout.
- **Evaluation** – Performance comparison of machine learning models.
- **Interpretation** – Explain model predictions using Feature Importance and SHAP.
- **About** – Project information.
""")