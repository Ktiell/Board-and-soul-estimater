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
    "Pine (indoor)": 2.00,
    "Walnut (indoor)": 7.00,
    "Maple (indoor)": 5.50,
    "Cedar (outdoor)": 3.50
}
templates = {
    "Floating Shelf": {"length": 24, "width": 6, "thickness": 0.75, "time": 0.75},
    "Sign": {"length": 18, "width": 12, "thickness": 0.5, "time": 0.5},
    "Table": {"length": 48, "width": 30, "thickness": 1.5, "time": 3.0},
}

# Sidebar
st.sidebar.header("Project Details")
project = st.sidebar.selectbox("Project Type", list(templates.keys()))
wood = st.sidebar.selectbox("Wood Type", list(wood_types.keys()))
d = templates[project]
length = st.sidebar.number_input("Length (inches)", 1, value=d["length"])
width = st.sidebar.number_input("Width (inches)", 1, value=d["width"])
thickness = st.sidebar.number_input("Thickness (inches)", 0.1, value=d["thickness"])
qty = st.sidebar.number_input("Quantity", 1, value=1)
rate = st.sidebar.number_input("Hourly Rate ($)", value=50.0)
time = st.sidebar.number_input("Build Time (hours)", value=d["time"])
profit = st.sidebar.slider("Profit Margin (%)", 0, 100, value=0)
tax = st.sidebar.number_input("Sales Tax (%)", min_value=0.0, value=0.0)

# Calculations
bf = (length *
