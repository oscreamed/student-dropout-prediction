import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Evaluation",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[2]
ASSETS = BASE_DIR / "app" / "assets"

st.title("Model Evaluation")

st.write("""
This page summarizes the performance of all machine learning models evaluated in this project.
""")

st.divider()

st.header("Performance Metrics")

comparison = pd.DataFrame({
    "Model":[
        "Logistic Regression",
        "Decision Tree",
        "XGBoost"
    ],
    "Accuracy":[
        74.40,
        71.35,
        79.60
    ]
})

st.dataframe(comparison, hide_index=True, use_container_width=True)

st.bar_chart(comparison.set_index("Model"))

st.divider()

st.header("Confusion Matrix")

st.image(
    ASSETS/"confusion_matrix.png",
    use_container_width=True
)

st.divider()

st.header("ROC Curve")

st.image(
    ASSETS/"roc_curve.png",
    use_container_width=True
)

st.divider()

st.success("""
**Best Model: XGBoost**

XGBoost achieved the highest accuracy (79.60%) and was selected as the final model for deployment.""")