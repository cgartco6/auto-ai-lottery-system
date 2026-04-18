import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

st.set_page_config(page_title="AI Simulation Dashboard")

st.title("AI Simulation Cluster")

st.write("System running successfully.")

st.success("Deployment OK")
