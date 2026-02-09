import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("diabetics_model.pkl", "rb") as file:
    model = pickle.load(file)


st.set_page_config(page_title="Diabetes Prediction", layout="centered")

# Title
st.title("🩺 Diabetes Prediction System")
st.write("Enter patient details to predict diabetes")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300)
bp = st.number_input("Blood Pressure", min_value=0, max_value=200)
skin = st.number_input("Skin Thickness", min_value=0, max_value=100)
insulin = st.number_input("Insulin Level", min_value=0, max_value=900)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=5.0)
age = st.number_input("Age", min_value=1, max_value=120)

# Predict button
if st.button("Predict"):

    input_data = np.array([[pregnancies, glucose, bp, skin,
                            insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error(" The person is likely to have Diabetes")
    else:
        st.success(" The person is NOT likely to have Diabetes")
