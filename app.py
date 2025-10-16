import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu

# ==============================
# Load Model
# ==============================
with open("xgb_employee_performance.pkl", "rb") as f:
    model_xgb = pickle.load(f)

# ==============================
# App Configuration
# ==============================
st.set_page_config(
    page_title="Employee Performance Prediction",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ==============================
# Sidebar Menu
# ==============================
with st.sidebar:
    selected = option_menu(
        "Employee Performance App",
        ["🏠 Home", "📊 Prediction", "ℹ️ About"],
        icons=["house", "bar-chart", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# ==============================
# Home Page
# ==============================
if selected == "🏠 Home":
    st.title("🧠 Employee Performance Prediction System")
    st.write("""
    Welcome to the **Employee Performance Prediction App** built using **Machine Learning (XGBoost)** 🚀.

    This app allows you to input employee information and get a predicted **performance rating**.
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/2881/2881142.png", width=250)
    st.markdown("---")
    st.markdown("👨‍💼 **Created by Neuronix AI Solutions**")
    st.caption("Team Leader: Ibrahim Abdelsattar")

# ==============================
# Prediction Page
# ==============================
elif selected == "📊 Prediction":
    st.title("📈 Predict Employee Performance")
    st.markdown("Fill in the details below to get the predicted performance rating:")

    # Input columns
    col1, col2 = st.columns(2)

    with col1:
        department = st.selectbox("Department", ["HR", "IT", "Finance", "Marketing", "Sales"])
        job_title = st.selectbox("Job Title", ["Manager", "Executive", "Analyst", "Developer", "Assistant"])
        location = st.selectbox("Location", ["Cairo", "Alexandria", "Remote", "Giza"])

    with col2:
        experience_years = st.number_input("Experience (Years)", min_value=0, max_value=40, step=1)
        status = st.selectbox("Status", ["Active", "Resigned", "Terminated"])
        work_mode = st.selectbox("Work Mode", ["On-site", "Hybrid", "Remote"])
        salary_inr = st.number_input("Salary (INR)", min_value=5000, max_value=300000, step=1000)

    st.markdown("---")
    predict_btn = st.button("🚀 Predict Performance")

    if predict_btn:
        # Manual label encoding (same order as training)
        dept_dict = {"HR": 0, "IT": 1, "Finance": 2, "Marketing": 3, "Sales": 4}
        job_dict = {"Manager": 0, "Executive": 1, "Analyst": 2, "Developer": 3, "Assistant": 4}
        loc_dict = {"Cairo": 0, "Alexandria": 1, "Remote": 2, "Giza": 3}
        status_dict = {"Active": 0, "Resigned": 1, "Terminated": 2}
        mode_dict = {"On-site": 0, "Hybrid": 1, "Remote": 2}

        input_data = np.array([[
            dept_dict[department],
            job_dict[job_title],
            loc_dict[location],
            experience_years,
            status_dict[status],
            mode_dict[work_mode],
            salary_inr
        ]])

        prediction = model_xgb.predict(input_data)[0]
        st.success(f"✅ Predicted Employee Performance Rating: **{int(prediction)} / 5**")

        # Interpretation
        if prediction >= 4:
            st.markdown("💪 This employee is **High Performing** and likely contributes strongly to the team.")
        elif prediction >= 3:
            st.markdown("🙂 This employee shows **Good Performance** with room for improvement.")
        else:
            st.markdown("⚠️ This employee might need **training or performance improvement plans**.")

# ==============================
# About Page
# ==============================
elif selected == "ℹ️ About":
    st.title("ℹ️ About the Project")
    st.write("""
    This project uses **XGBoost**, a powerful machine learning algorithm,
    to predict the performance rating of employees based on their data such as:

    - Department  
    - Job Title  
    - Location  
    - Experience  
    - Status  
    - Work Mode  
    - Salary  

    ---
    👨‍💻 **Developed by:** Ibrahim Abdelsattar  
    🧩 **Team:** Neuronix AI Solutions  
    🔗 **Field:** AI Engineering
    """)

    st.image("https://cdn-icons-png.flaticon.com/512/4727/4727253.png", width=250)
