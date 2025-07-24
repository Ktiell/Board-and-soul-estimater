import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Board & Soul Estimator", layout="centered")

# Inject custom CSS for branding
st.markdown("""
<style>
body {
    background-color: #f5f5dc;
}
section.main > div {
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
h1, h2, h3, h4 {
    color: #4f6f52;
    font-family: 'Segoe UI', sans-serif;
}
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 1rem 0;
}
.stButton>button {
    background-color: #4f6f52;
    color: white;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    border: none;
}
.stDownloadButton>button {
    background-color: #4f6f52;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# Logo and Title
st.image("https://i.imgur.com/fMMms9B.png", width=200)
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>Board & Soul Estimator</h1>", unsafe_allow_html=True)
st.markdown("<hr style='margin-top: 0;'>", unsafe_allow_html=True)

# Wood and template data
wood_types = {
    "Pine (indoor)": 2.00,
    "Walnut (indoor)": 7.00,
    "Maple (indoor)": 5.50,
    "Cedar (outdoor)": 3.50
}
project_templates = {
    "Floating Shelf": {"length": 24, "width": 6, "thickness": 0.75, "time": 0.75},
    "Sign": {"length": 18, "width": 12, "thickness": 0.5, "time": 0.5},
    "Table": {"length": 48, "width": 30, "thickness": 1.5, "time": 3.0},
}

# Sidebar inputs
st.sidebar
