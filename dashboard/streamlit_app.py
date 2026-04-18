import streamlit as st
st.set_option("browser.gatherUsageStats", False)

import pandas as pd
import numpy as np

st.title("AI Simulation Dashboard")

data = pd.DataFrame(
    np.random.randint(1,50,(50,6)),
    columns=["N1","N2","N3","N4","N5","N6"]
)

st.write("Simulation output")

st.dataframe(data)

st.bar_chart(data)
