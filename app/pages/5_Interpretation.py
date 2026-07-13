import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Interpretation",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[2]
ASSETS = BASE_DIR / "app/assets"

st.title("Model Interpretation")

st.write("""
Model interpretation helps explain which features have the greatest influence on predicting whether a student will graduate or drop out.
""")

st.divider()

st.header("Feature Importance")

st.image(
    ASSETS/"feature_importance.png",
    use_container_width=True
)

st.write("""
The Feature Importance plot shows the variables that contribute the most to the XGBoost prediction.
""")

st.divider()

st.header("SHAP Summary Plot")

st.image(
    ASSETS/"shap_summary.png",
    use_container_width=True
)

st.write("""
The SHAP Summary Plot explains the contribution of each feature to the prediction results.
Features such as GPA, CGPA, Attendance Rate, and Study Hours per Day have the strongest impact on the model.
""")

st.divider()

st.header("Business Insights")

st.info("""
• Students with low GPA and CGPA have a higher dropout risk.

• Low attendance is an important indicator of academic problems.

• Students with fewer study hours require additional academic support.

• Early intervention programs can reduce dropout rates.
""")