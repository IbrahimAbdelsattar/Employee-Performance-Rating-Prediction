import streamlit as st
import pickle
import numpy as np

# ==============================
# Load Trained XGBoost Model
# ==============================
with open("xgb_employee_performance.pkl", "rb") as f:
    model_xgb = pickle.load(f)

# ==============================
# Streamlit Page Configuration
# ==============================
st.set_page_config(
    page_title="Employee Performance Prediction",
    page_icon="🧠",
    layout="wide"
)

# ==============================
# App Header
# ==============================
st.title("🧠 Employee Performance Prediction System")
st.markdown("""
This app uses a trained **XGBoost** model to predict an employee's performance rating  
based on their role, experience, and employment status.
""")
st.divider()

# ==============================
# Input Form
# ==============================
st.header("📊 Enter Employee Details")

col1, col2 = st.columns(2)

with col1:
    department = st.selectbox("Department", [
        "IT", "Sales", "Operations", "Marketing", "Finance", "HR", "R&D"
    ])

    job_title = st.selectbox("Job Title", [
        "Software Engineer", "Sales Executive", "Operations Executive", "Data Analyst",
        "Marketing Executive", "Account Manager", "Accountant", "DevOps Engineer",
        "Logistics Coordinator", "HR Executive", "SEO Specialist",
        "Business Development Manager", "IT Manager", "Financial Analyst",
        "Research Scientist", "Talent Acquisition Specialist", "Supply Chain Manager",
        "Content Strategist", "CTO", "Product Developer", "Finance Manager",
        "HR Manager", "Sales Director", "Operations Director", "Lab Technician",
        "Brand Manager", "CFO", "HR Director", "Innovation Manager"
    ])

    location = st.text_input("Location (e.g., Lake Michael, Congo)", placeholder="Enter employee location")

with col2:
    experience_years = st.number_input("Experience (Years)", min_value=0, max_value=40, step=1)
    status = st.selectbox("Status", ["Active", "Resigned", "Retired", "Terminated"])
    work_mode = st.selectbox("Work Mode", ["On-site", "Remote"])
    salary_inr = st.number_input("Salary (INR)", min_value=10000, max_value=3000000, step=1000)

# ==============================
# Predict Button
# ==============================
st.divider()
if st.button("🚀 Predict Performance"):
    # Label encoding manually (based on training order)
    dept_dict = {"IT": 0, "Sales": 1, "Operations": 2, "Marketing": 3, "Finance": 4, "HR": 5, "R&D": 6}
    job_dict = {
        "Software Engineer": 0, "Sales Executive": 1, "Operations Executive": 2, "Data Analyst": 3,
        "Marketing Executive": 4, "Account Manager": 5, "Accountant": 6, "DevOps Engineer": 7,
        "Logistics Coordinator": 8, "HR Executive": 9, "SEO Specialist": 10,
        "Business Development Manager": 11, "IT Manager": 12, "Financial Analyst": 13,
        "Research Scientist": 14, "Talent Acquisition Specialist": 15, "Supply Chain Manager": 16,
        "Content Strategist": 17, "CTO": 18, "Product Developer": 19, "Finance Manager": 20,
        "HR Manager": 21, "Sales Director": 22, "Operations Director": 23, "Lab Technician": 24,
        "Brand Manager": 25, "CFO": 26, "HR Director": 27, "Innovation Manager": 28
    }
    status_dict = {"Active": 0, "Resigned": 1, "Retired": 2, "Terminated": 3}
    mode_dict = {"On-site": 0, "Remote": 1}

    # Location encoded as text length proxy (simplified encoding)
    location_encoded = len(location)

    input_data = np.array([[
        dept_dict[department],
        job_dict[job_title],
        location_encoded,
        experience_years,
        status_dict[status],
        mode_dict[work_mode],
        salary_inr
    ]])

    # Predict
    prediction = model_xgb.predict(input_data)[0]

    st.success(f"✅ Predicted Employee Performance Rating: **{int(prediction)} / 5**")

    # Interpretation
    if prediction >= 4:
        st.info("💪 This employee is **High Performing** and likely a top contributor to the team.")
    elif prediction >= 3:
        st.warning("🙂 This employee shows **Good Performance** with room for improvement.")
    else:
        st.error("⚠️ This employee might need **training or performance improvement plans**.")

# ==============================
# Footer
# ==============================
st.divider()
st.caption("Developed by **Ibrahim Abdelsattar** | Neuronix AI Solutions 🧠")
