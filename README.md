import streamlit as st
import pandas as pd
from xgboost import XGBClassifier
from pathlib import Path

st.set_page_config(
    page_title="Prediction",
    page_icon="🤖",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[2]

model = XGBClassifier()
model.load_model(BASE_DIR / "models" / "best_model.json")

st.title("Student Dropout Prediction")

st.write("""
Enter the student information below and click **Predict**
to estimate whether the student is more likely to **Graduate**
or **Dropout**.

The prediction is generated using the Logistic Regression model
selected during the model evaluation process.
""")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Student Information")

    age = st.number_input(
        "Age",
        min_value=17.0,
        max_value=40.0,
        value=20.0
    )

    gender = st.selectbox(
        "Gender",
        [0, 1],
        format_func=lambda x: "Female" if x == 0 else "Male"
    )

    family_income = st.number_input(
        "Family Income",
        min_value=0.0,
        value=5000.0
    )

    internet = st.selectbox(
        "Internet Access",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    study_hours = st.number_input(
        "Study Hours per Day",
        min_value=0.0,
        max_value=24.0,
        value=4.0
    )

    attendance = st.slider(
        "Attendance Rate (%)",
        0.0,
        100.0,
        80.0
    )

    assignment_delay = st.number_input(
        "Assignment Delay (Days)",
        min_value=0,
        value=2
    )

with col2:

    st.subheader("Academic Information")

    travel_time = st.number_input(
        "Travel Time (Minutes)",
        min_value=0.0,
        value=30.0
    )

    parttime = st.selectbox(
        "Part-Time Job",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    scholarship = st.selectbox(
        "Scholarship",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    stress = st.slider(
        "Stress Index",
        0.0,
        10.0,
        5.0
    )

    gpa = st.number_input(
        "GPA",
        min_value=0.0,
        max_value=4.0,
        value=3.00
    )

    semester_gpa = st.number_input(
        "Semester GPA",
        min_value=0.0,
        max_value=4.0,
        value=3.00
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=4.0,
        value=3.00
    )

    semester = st.selectbox(
        "Semester",
        [0, 1, 2, 3],
        format_func=lambda x: f"Semester {x+1}"
    )

    department = st.selectbox(
        "Department",
        [0, 1, 2, 3, 4],
        format_func=lambda x: f"Department {x+1}"
    )

    parent = st.selectbox(
        "Parental Education",
        [0, 1, 2, 3],
        format_func=lambda x: f"Level {x+1}"
    )

# ==========================================================
# PREDICTION
# ==========================================================

if st.button("Predict", use_container_width=True):

    input_data = pd.DataFrame([[

        age,
        gender,
        family_income,
        internet,
        study_hours,
        attendance,
        assignment_delay,
        travel_time,
        parttime,
        scholarship,
        stress,
        gpa,
        semester_gpa,
        cgpa,
        semester,
        department,
        parent

    ]], columns=[

        "Age",
        "Gender",
        "Family_Income",
        "Internet_Access",
        "Study_Hours_per_Day",
        "Attendance_Rate",
        "Assignment_Delay_Days",
        "Travel_Time_Minutes",
        "Part_Time_Job",
        "Scholarship",
        "Stress_Index",
        "GPA",
        "Semester_GPA",
        "CGPA",
        "Semester",
        "Department",
        "Parental_Education"

    ])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    graduate_prob = probability[0] * 100
    dropout_prob = probability[1] * 100

    st.divider()

    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Graduate Probability",
            f"{graduate_prob:.2f}%"
        )

    with col2:
        st.metric(
            "Dropout Probability",
            f"{dropout_prob:.2f}%"
        )

    if prediction == 0:

        st.success("Prediction Result: Graduate")

st.info("""
The model predicts that the student is likely to successfully complete
their study program.

Maintaining consistent academic performance and attendance is recommended
to sustain this outcome.
""")

    else:

        st.error("Prediction Result: Dropout")

st.warning("""
The model predicts that the student has a relatively higher risk of dropping out.

Additional academic support and continuous monitoring may help reduce this risk.
""")