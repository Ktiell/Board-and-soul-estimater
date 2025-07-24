import streamlit as st
import pandas as pd

st.set_page_config(page_title="Board & Soul Estimator", layout="centered")

# Brand styling (trimmed for safety)
st.markdown("""
<style>
body { background-color: #f5f5dc; }
section.main > div {
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
h1, h3 { color: #4f6f52; font-family: 'Segoe UI', sans-serif; }
.stDownloadButton>button, .stButton>button {
    background-color: #4f6f52;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# Text banner
st.markdown("""
<div style='text-align: center; padding: 10px 0 0 0;'>
    <h1>🪵 Board & Soul</h1>
    <h3>Handmade Estimator</h3>
</div>
<hr>
""", unsafe_allow_html=True)

# Data
wood_types = {
    "Pine (indoor)": 2
