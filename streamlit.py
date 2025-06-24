import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"


st.set_page_config(page_title="Telco Churn Predictor", layout="centered")

st.title("📞 Telco Customer Churn Prediction")

st.markdown("Fill in the customer details below to predict if they are likely to churn.")

gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=1)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
PaymentMethod = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check",
    "Bank transfer (automatic)", "Credit card (automatic)"
])
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
TotalCharges = st.text_input("Total Charges", "70.0")
customerID = st.text_input("Customer ID", "1234-ABCDE")

# Submit to FastAPI
if st.button("Predict Churn"):
    data = {
        "customerID": customerID,
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "PaperlessBilling": PaperlessBilling,
        "Contract": Contract,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    try:
        # Adjust this if you're running FastAPI on a remote server
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['Prediction']}")
            st.info(f"Churn Probability: {result['Probability']:.2f}")

        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Connection error: {e}")
