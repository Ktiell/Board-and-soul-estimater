import streamlit as st
import pandas as pd

st.title("Board & Soul Project Estimator")

wood_types = {
    "Pine (indoor)": 2.00,
    "Walnut (indoor)": 7.00,
    "Maple (indoor)": 5.50,
    "Cedar (outdoor)": 3.50
}
project_types = ["Floating Shelf", "Sign", "Table"]

st.sidebar.header("Project Details")
project_type = st.sidebar.selectbox("Project Type", project_types)
wood_type = st.sidebar.selectbox("Wood Type", list(wood_types.keys()))
length = st.sidebar.number_input("Length (inches)", min_value=1)
width = st.sidebar.number_input("Width (inches)", min_value=1)
thickness = st.sidebar.number_input("Thickness (inches)", min_value=0.1, value=0.75)
quantity = st.sidebar.number_input("Quantity", min_value=1, value=1)
hourly_rate = st.sidebar.number_input("Hourly Rate ($)", value=50.0)
build_time = st.sidebar.number_input("Build Time (hours)", value=1.0)
sales_tax_rate = st.sidebar.number_input("Sales Tax (%)", min_value=0.0, value=0.0)

# Board feet and cost
board_feet = (length * width * thickness) / 144 * quantity
material_cost = board_feet * wood_types[wood_type]
labor_cost = hourly_rate * build_time
subtotal = material_cost + labor_cost
sales_tax = subtotal * (sales_tax_rate / 100)
total_price = subtotal + sales_tax

# Results
st.subheader("Estimate Summary")
st.write(f"**Material Cost:** ${material_cost:.2f}")
st.write(f"**Labor Cost:** ${labor_cost:.2f}")
st.write(f"**Subtotal:** ${subtotal:.2f}")
st.write(f"**Sales Tax:** ${sales_tax:.2f}")
st.write(f"**Total Estimated Price:** ${total_price:.2f}")
