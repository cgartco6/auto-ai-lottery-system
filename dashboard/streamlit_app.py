import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="AI Simulation Dashboard",
    layout="wide"
)

st.title("AI Lottery Simulation System")

st.write("Monte Carlo Simulation Output")

data = pd.DataFrame(
    np.random.randint(1,50,(100,6)),
    columns=["N1","N2","N3","N4","N5","N6"]
)

st.dataframe(data)

st.bar_chart(data)
