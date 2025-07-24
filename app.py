import streamlit as st
import pandas as pd

st.set_page_config(page_title="Board & Soul Estimator", layout="centered")

st.markdown("""
<style>
body { background-color: #f5f5dc; }
section.main > div {
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
h1, h3 {
    color: #4f6f52;
    font-family: 'Segoe UI', sans-serif;
}
.stButton>button, .stDownloadButton>button {
    background-color: #4f6f52;
    color: white;
    border-radius: 8px;
    padding: 0.5rem 1rem;
}
</style>
""", unsafe_allow_html=True)

# Text banner logo
st.markdown("""
<div style='text-align: center; padding-top: 10px;'>
    <h1>🪵 Board & Soul</h1>
    <h3>Handmade Estimator</h3>
</div>
<hr>
""", unsafe_allow_html=True)

wood_types = {
    "Pine (indoor)": 2.00,
    "Walnut (indoor)": 7.00,
    "Maple (indoor)": 5.50,
    "Cedar (outdoor)": 3.50
}

project_templates = {
    "Floating Shelf": {"length": 24, "width": 6, "thickness": 0.75, "time": 0.75},
    "Sign": {"length": 18, "width": 12, "thickness": 0.5, "time": 0.5},
    "Table": {"length": 48, "width": 30, "thickness": 1.5, "time": 3.0}
}

st.sidebar.header("Project Details")
project_type = st.sidebar.selectbox("Project Type", list(project_templates.keys()))
wood_type = st.sidebar.selectbox("Wood Type", list(wood_types.keys()))
default = project_templates[project_type]

length = st.sidebar.number_input("Length (inches)", min_value=1, value=default["length"])
width = st.sidebar.number_input("Width (inches)", min_value=1, value=default["width"])
thickness = st.sidebar.number_input("Thickness (inches)", min_value=0.1, value=default["thickness"])
quantity = st.sidebar.number_input("Quantity", min_value=1, value=1)
hourly_rate = st.sidebar.number_input("Hourly Rate ($)", value=50.0)
build_time = st.sidebar.number_input("Build Time (hours)", value=default["time"])
profit_margin = st.sidebar.slider("Profit Margin (%)", 0, 100, 0)
sales_tax_rate = st.sidebar.number_input("Sales Tax (%)", min_value=0.0, value=0.0)

board_feet = (length * width * thickness) / 144 * quantity
material_cost = board_feet * wood_types[wood_type]
labor_cost = hourly_rate * build_time
subtotal = material_cost + labor_cost
markup = subtotal * (profit_margin / 100)
subtotal_with_profit = subtotal + markup
sales_tax = subtotal_with_profit * (sales_tax_rate / 100)
total_price = subtotal_with_profit + sales_tax

st.subheader("Estimate Summary")
st.write(f"**Material Cost:** ${material_cost:.2f}")
st.write(f"**Labor Cost:** ${labor_cost:.2f}")
st.write(f"**Subtotal (with profit):** ${subtotal_with_profit:.2f}")
st.write(f"**Sales Tax:** ${sales_tax:.2f}")
st.write(f"**Total Estimated Price:** ${total_price:.2f}")

estimate = pd.DataFrame([{
    "Project": project_type,
    "Wood Type": wood_type,
    "Length": length,
    "Width": width,
    "Thickness": thickness,
    "Quantity": quantity,
    "Material Cost": material_cost,
    "Labor Cost": labor_cost,
    "Profit Margin (%)": profit_margin,
    "Subtotal (w/ profit)": subtotal_with_profit,
    "Sales Tax (%)": sales_tax_rate,
    "Total Price": total_price
}])

csv = estimate.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Estimate (CSV)", csv, file_name="estimate.csv", mime="text/csv")
