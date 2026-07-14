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

st.markdown("""
This page summarizes the performance of the machine learning models evaluated
during the development process.
""")

st.header("Model Performance")

comparison = pd.DataFrame({
    "Model":[
        "Logistic Regression",
        "XGBoost",
        "Decision Tree"
    ],
    "Accuracy":[
        79.80,
        79.60,
        78.60
    ]
})

st.dataframe(
    comparison,
    hide_index=True,
    use_container_width=True
)

st.bar_chart(
    comparison.set_index("Model")
)

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

st.header("Evaluation Summary")

st.success("""
Logistic Regression achieved the best overall performance among the evaluated models.

The model obtained the highest accuracy and ROC-AUC score while providing
a balanced classification performance and good interpretability.

Therefore, Logistic Regression was selected as the final model for deployment.
""")