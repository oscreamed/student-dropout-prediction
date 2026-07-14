import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Interpretation",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[2]
ASSETS = BASE_DIR / "app" / "assets"

st.title("Model Interpretation")

st.markdown("""
Model interpretation helps identify the variables that have the greatest influence
on student dropout prediction.
""")

st.divider()

st.header("Feature Importance")

st.image(
    ASSETS/"feature_importance.png",
    use_container_width=True
)

st.write("""
Feature Importance indicates that variables related to academic performance,
attendance, and study behavior contribute significantly to the prediction results.
""")

st.divider()

st.header("SHAP Interpretation")

st.image(
    ASSETS/"shap_summary.png",
    use_container_width=True
)

st.write("""
SHAP values provide a detailed explanation of how each feature contributes
to individual predictions.

Although SHAP visualization is generated using XGBoost due to its compatibility
with tree-based interpretation techniques, Logistic Regression remains the
final model selected for deployment based on the evaluation results.
""")