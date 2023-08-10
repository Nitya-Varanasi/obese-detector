import streamlit as st
import joblib
st.title("Weight Predictor")
weight = st.slider('Weight(in kgs)', 0, 100, 50)
height = st.slider('Height(in cms)', 0, 200, 50)
model = joblib.load('model_new')
result = model.predict([[weight, height]])[0]

if st.button("Predict"):
  st.write(f"You are {result}")
