import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Exploratory Data Analysis",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[2]
ASSETS = BASE_DIR / "app" / "assets"

st.title("Exploratory Data Analysis")

st.divider()

df = pd.read_csv(BASE_DIR / "data" / "raw" / "student_dropout_dataset_v3.csv")

st.header("Descriptive Statistics")

st.write(
    "The descriptive statistics summarize the numerical variables contained in the dataset."
)

st.dataframe(df.describe(), use_container_width=True)

st.divider()

st.header("Missing Values")

st.write(
    "The table below presents the number of missing values for each feature."
)

st.dataframe(
    df.isnull().sum().to_frame("Missing Values"),
    use_container_width=True
)

st.divider()

st.header("Correlation Matrix")

st.write("""
    The correlation heatmap illustrates the relationships among numerical features.

    GPA, Semester GPA, and CGPA show strong positive correlations because they
    represent similar aspects of academic performance. In contrast, Stress Index
    is positively associated with dropout risk, while GPA has a negative
    relationship with dropout.
""")

st.image(
    ASSETS / "correlation_heatmap.png",
    use_container_width=True
)