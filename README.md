# 🧠 Employee Performance Prediction System

## 📋 Overview
The **Employee Performance Prediction System** is a Machine Learning and Deep Learning project designed to **predict employee performance ratings** based on workplace and personal data.

This project aims to support HR teams and decision-makers by identifying:
- High-performing employees for recognition and promotion.
- Underperforming employees who may need training or support.
- Patterns and insights that can improve overall workforce management.

---

## 🚀 Key Features
- 🔹 Predicts employee performance rating on a scale of **1–5**.
- 🔹 Built with **XGBoost** for high accuracy.
- 🔹 Includes **Deep Neural Network (DNN)** implementation for experimentation.
- 🔹 **Clean, modern Streamlit interface** for easy deployment.
- 🔹 **Categorical encoding** using LabelEncoder.
- 🔹 **Data scaling**, training, validation, and testing included.
- 🔹 **Confusion matrix visualization** and **classification reports** for performance evaluation.
- 🔹 Ready for **deployment and integration** in HR dashboards.

---

## 🧠 Machine Learning Pipeline

### 1️⃣ Data Preprocessing
- Columns encoded using **LabelEncoder** for categorical features:
  - Department  
  - Job Title  
  - Location  
  - Status  
  - Work Mode  
- Numerical columns scaled using **StandardScaler**.

### 2️⃣ Model Training
- **Models Used:**
  - Logistic Regression  
  - Random Forest  
  - XGBoost  
  - Deep Neural Network (DNN)
- Each model trained and validated separately.
- Evaluation metrics include:
  - Accuracy
  - Precision
  - Recall
  - F1-Score

### 3️⃣ Model Evaluation
- Classification reports for all models.
- Confusion matrix visualizations.
- XGBoost selected as the **final production model** due to superior accuracy.

---

## 🌐 Streamlit Deployment

The project includes a **Streamlit web app** that allows users to input employee details and get an instant performance prediction.

### 🎨 App Features
- Modern UI with side navigation (Home, Prediction, About).
- Interactive dropdowns and numeric fields for input.
- Real-time performance prediction using trained XGBoost model.
- Text-based interpretation of results for better HR understanding.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/employee-performance-prediction.git
cd employee-performance-prediction
'''

### 2️⃣ Install Dependencies
pip install -r requirements.txt

🧩 Project Structure
📦 employee-performance-prediction
│
├── app.py                        # Streamlit deployment script
├── model_training.ipynb          # Jupyter notebook for model training
├── xgb_employee_performance.pkl  # Saved XGBoost model
├── requirements.txt              # Dependencies list
├── README.md                     # Project documentation
└── data/
    └── employee_performance.csv  # Dataset used for training


📊 Example Input Fields

Department: HR / IT / Finance / Marketing / Sales

Job Title: Manager / Executive / Analyst / Developer / Assistant

Location: Cairo / Alexandria / Remote / Giza

Experience (Years): Integer (0–40)

Status: Active / Resigned / Terminated

Work Mode: On-site / Hybrid / Remote

Salary (INR): Integer (5,000 – 300,000)


✅ Predicted Employee Performance Rating: 4 / 5
💪 This employee is High Performing and likely contributes strongly to the team.


🧑‍💻 Developed By

👨‍💻 Ibrahim Abdelsattar
AI Engineer | Team Leader at Neuronix AI Solutions
