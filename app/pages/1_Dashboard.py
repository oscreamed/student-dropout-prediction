import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

st.title("Dataset Dashboard")

st.markdown("""
This page provides an overview of the dataset used for predicting student dropout.

The dataset contains academic and socio-economic information collected from students
and is used to train and evaluate the machine learning models developed in this project.
""")

df = pd.read_csv("data/raw/student_dropout_dataset_v3.csv")

st.divider()

st.header("Dataset Overview")

st.write("The table below displays the first five records of the dataset.")

st.dataframe(df.head(), use_container_width=True)

st.divider()

st.header("Dataset Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Number of Features", df.shape[1] - 1)
col3.metric("Target Variable", "Dropout")

st.divider()

st.header("Target Distribution")

st.write("The chart below illustrates the distribution of graduate and dropout students.")

target = (
    df["Dropout"]
    .replace({0: "Graduate", 1: "Dropout"})
    .value_counts()
)

st.bar_chart(target)