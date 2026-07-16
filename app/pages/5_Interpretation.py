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
Feature Importance identifies which variables contribute the most to the
prediction process.

The analysis shows that GPA is the most influential feature, followed by
Stress Index, Attendance Rate, Semester GPA, Travel Time Minutes, and
Assignment Delay Days. These findings indicate that academic performance
plays the most significant role in predicting student dropout.
""")

st.divider()

st.header("SHAP Interpretation")

st.image(
    ASSETS/"shap_summary.png",
    use_container_width=True
)

st.write("""
The SHAP Summary Plot explains how each feature influences the model's
predictions.

Higher GPA values generally contribute toward predicting Graduate, whereas
higher Stress Index values tend to increase the probability of Dropout.
Overall, GPA remains the most influential feature, followed by Stress Index
and Attendance Rate.
""")