import streamlit as st
import pandas as pd

from pipeline.generate_predictions import generate

st.title("AI PowerBall Prediction Dashboard")

top13, top6 = generate()


st.header("Top 6 Strongest Predictions")

df6 = pd.DataFrame(
    [list(x[0]) + [x[1]] for x in top6],
    columns=["N1","N2","N3","N4","N5","Score"]
)

st.dataframe(df6)


st.header("Top 13 Prediction Pool")

df13 = pd.DataFrame(
    [list(x[0]) + [x[1]] for x in top13],
    columns=["N1","N2","N3","N4","N5","Score"]
)

st.dataframe(df13)
