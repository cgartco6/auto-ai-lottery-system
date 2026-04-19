import streamlit as st
from pipeline.generate_predictions import generate

st.title("PowerBall AI Prediction Dashboard")

top13, top6 = generate()

st.subheader("Top 6 Strongest Predictions")
st.write(top6)

st.subheader("Top 13 Prediction Pool")
st.write(top13)
