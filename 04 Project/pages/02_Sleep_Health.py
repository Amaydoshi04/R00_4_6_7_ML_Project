import streamlit as st
import pickle
import numpy as np

from support import (
    preprocessor,
    le_gender_mapping,
    le_occupation_mapping,
    le_bmi_category_mapping,
    ss_age,
    ss_sleep_duration,
    ss_quality_of_sleep,
    ss_physical_activity_level,
    ss_stress_level,
    ss_heart_rate,
    ss_daily_steps,
    ss_systolic_pressure,
    ss_diastolic_pressure,
    le_sleep_disorder_mapping,
)


st.title("Take the Sleep Savvy Quiz")
st.markdown(
    "### Answer the following questions to get a better understanding of your sleep health."
)

with st.form("Sleep Health"):
    name = st.text_input("Enter your name")

    gender = st.radio("Select your Gender", ["Male", "Female"])

    age = st.number_input("Enter your age")

    occupation = st.selectbox(
        "What is your occupation?",
        [
            "Software Engineer",
            "Doctor",
            "Sales Representative",
            "Teacher",
            "Nurse",
            "Engineer",
            "Accountant",
            "Scientist",
            "Lawyer",
            "Salesperson",
            "Manager",
        ],
    )

    sleep_duration = st.slider("How many hours do you sleep per night?", 1, 12, 6)

    sleep_quality = st.slider("Rate your sleep quality", 1, 10, 7)

    activity_level = st.slider("How active are you during the day?", 1, 10, 2, 1)

    stress_level = st.slider("Rate your stress level", 1, 10, 5)

    bmi_category = st.selectbox(
        "What is your BMI category?", ["Normal Weight", "Overweight", "Obese"]
    )

    heart_rate = st.slider("Enter your resting heart rate", 40, 200, 60)

    steps_per_day = st.slider("How many steps do you take per day?", 100, 30000, 5000)

    systolic_bp = st.slider("Enter your Systolic Blood Pressure", 80, 300, 120)

    diastolic_bp = st.slider("Enter your Diastolic Blood Pressure", 50, 200, 80)

    tnc = st.checkbox("I agree to the Terms and Conditions")

    data = {
        "gender": gender,
        "age": age,
        "occupation": occupation,
        "sleep_duration": sleep_duration,
        "sleep_quality": sleep_quality,
        "activity_level": activity_level,
        "stress_level": stress_level,
        "bmi_category": bmi_category,
        "heart_rate": heart_rate,
        "steps_per_day": steps_per_day,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "tnc": tnc,
        "name": name,
    }

    submit = st.form_submit_button("Submit")

if submit:
    # st.write(data)
    st.success("Thank you for submitting the form!")
    st.write(
        "We will now analyze your responses to provide you with insights into your sleep health."
    )
    preprocessed_data = preprocessor(
        data,
        le_gender_mapping,
        le_occupation_mapping,
        le_bmi_category_mapping,
        ss_age,
        ss_sleep_duration,
        ss_quality_of_sleep,
        ss_physical_activity_level,
        ss_stress_level,
        ss_heart_rate,
        ss_daily_steps,
        ss_systolic_pressure,
        ss_diastolic_pressure,
    )

    mapping = {"Insomnia": 0, "None": 1, "Sleep Apnea": 2}

    op = []

    with open("gnbmodel.pkl", "rb") as f:
        model = pickle.load(f)

        prediction = model.predict(
            np.array(list(preprocessed_data.values())).reshape(1, -1)
        )

        st.write("Naive Bayes Prediction: ")
        st.write(prediction)

        op.append(prediction)

    with open("dtcG5model.pkl", "rb") as f:
        model = pickle.load(f)

        prediction = model.predict(
            np.array(list(preprocessed_data.values())).reshape(1, -1)
        )

        st.write("Decision Tree Classifier Prediction: ")
        st.write(prediction)

        op.append(prediction)

    with open("abcmodel.pkl", "rb") as f:
        model = pickle.load(f)

        prediction = model.predict(
            np.array(list(preprocessed_data.values())).reshape(1, -1)
        )

        st.write("AdaBoost Classifier Prediction: ")
        st.write(prediction)

        op.append(prediction)

    with open("svmmodel.pkl", "rb") as f:
        model = pickle.load(f)

        prediction = model.predict(
            np.array(list(preprocessed_data.values())).reshape(1, -1)
        )

        st.write("SVM Classifier Prediction: ")
        st.write(prediction)

    op.append(prediction)

    with open("knnmodel.pkl", "rb") as f:
        model = pickle.load(f)

        prediction = model.predict(
            np.array(list(preprocessed_data.values())).reshape(1, -1)
        )

        st.write("KNN Classifier Prediction: ")
        st.write(prediction)

    op.append(prediction)

    st.write("Final Prediction: ")
    for i in range(len(op)):
        if op[i] == 0:
            st.write("Insomnia")
        elif op[i] == 1:
            st.write("None")
        else:
            st.write("Sleep Apnea")
