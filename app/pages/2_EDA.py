import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Exploratory Data Analysis",
    layout="wide"
)

st.title("Exploratory Data Analysis")

df = pd.read_csv("data/raw/student_dropout_dataset_v3.csv")

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

st.write(
    "The correlation heatmap illustrates the relationships among numerical features."
)

st.image(
    ASSETS/"correlation_heatmap.png",
    use_container_width=True
)

st.pyplot(fig)