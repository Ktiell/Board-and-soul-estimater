import streamlit as st
import pandas as pd

st.title("Board & Soul Project Estimator")

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

st.sidebar.header("Project Details")
project_type = st.sidebar.selectbox("Project Type", list(project_templates.keys()))
wood_type = st.sidebar.selectbox("Wood Type", list(wood_types.keys()))

# Load template defaults
default = project_templates[project_type]
length = st.sidebar.number_input("Length (inches)", min_value=1, value=default["length"])
width = st.sidebar.number_input("Width (inches)", min_value=1, value=default["width"])
thickness = st.sidebar.number_input("Thickness (inches)", min_value=0.1, value=default["thickness"])
quantity = st.sidebar.number_input("Quantity", min_value=1, value=1)
hourly_rate = st.sidebar.number_input("Hourly Rate ($)", value=50.0)
build_time = st.sidebar.number_input("Build Time (hours)", value=default["time"])
profit_margin = st.sidebar.slider("Profit Margin (%)", min_value=0, max_value=100, value=0)
sales_tax_rate = st.sidebar.number_input("Sales Tax (%)", min_value=0.0, value=0.0)

# Cost calculations
board_feet = (length * width * thickness) / 144 * quantity
material_cost = board_feet * wood_types[wood_type]
labor_cost = hourly_rate * build_time
subtotal = material_cost + labor_cost
markup = subtotal * (profit_margin / 100)
subtotal_with_profit = subtotal + markup
sales_tax = subtotal_with_profit * (sales_tax_rate / 100)
total_price = subtotal_with_profit + sales_tax

# Display estimate
st.subheader("Estimate Summary")
st.write(f"**Material Cost:** ${material_cost:.2f}")
st.write(f"**Labor Cost:** ${labor_cost:.2f}")
st.write(f"**Subtotal (with profit):** ${subtotal_with_profit:.2f}")
st.write(f"**Sales Tax:** ${sales_tax:.2f}")
st.write(f"**Total Estimated Price:** ${total_price:.2f}")

# CSV download
estimate_data = pd.DataFrame([{
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

csv = estimate_data.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Estimate (CSV)", csv, file_name="estimate.csv", mime="text/csv")
