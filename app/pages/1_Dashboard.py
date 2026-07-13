import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[2]
df = pd.read_csv(BASE_DIR / "data" / "raw" / "student_dropout_dataset_v3.csv")

st.title("Dashboard")

st.write("""This dashboard provides an overview of the dataset used for predicting student graduation and dropout.""")

st.divider()

st.header("Dataset Overview")

st.dataframe(df.head(), use_container_width=True)

st.divider()

st.header("Dataset Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Total Features", df.shape[1]-1)
col3.metric("Target Variable", "Dropout")

st.divider()

st.header("Target Distribution")

target = df["Dropout"].replace({
    0: "Graduate",
    1: "Dropout"
})

st.bar_chart(target.value_counts())