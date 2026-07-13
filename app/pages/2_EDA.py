import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

st.set_page_config(
    page_title="EDA",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[2]

df = pd.read_csv(BASE_DIR / "data/raw/student_dropout_dataset_v3.csv")

st.title("Exploratory Data Analysis")

st.write("""This page presents descriptive statistics and exploratory analysis of the dataset.""")

st.divider()

st.header("Descriptive Statistics")

st.dataframe(df.describe(), use_container_width=True)

st.divider()

st.header("Missing Values")

missing = df.isnull().sum().to_frame("Missing Values")

st.dataframe(missing)

st.divider()

st.header("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(12,8))

sns.heatmap(
    df.select_dtypes(include="number").corr(),
    cmap="Blues",
    ax=ax
)

st.pyplot(fig)