import tensorflow as tf
import joblib
from schema.customer_data import CustomerData
import pandas as pd


model = tf.keras.models.load_model("models/churn_model.keras")
scaler = joblib.load("models/scaler.pkl")

MODEL_VERSION ="1.0.0"



def preprocess(data: CustomerData):
    df = pd.DataFrame([data.dict()])
    df.drop('customerID', axis=1, inplace=True)
    df.replace('No phone service', 'No', inplace=True)
    df.replace('No internet service', 'No', inplace=True)

    binary_cols = [
        'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
        'StreamingMovies', 'PaperlessBilling', 'SeniorCitizen'
    ]
    df[binary_cols] = df[binary_cols].replace({"Yes": 1, "No": 0})
    df["gender"] = df["gender"].replace({"Male": 1, "Female": 0})
    
    # Fix NaNs before scaling
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.fillna(0, inplace=True)

    # Scaling
    num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    df[num_cols] = scaler.transform(df[num_cols])

    # Encoding
    cat_cols = ['InternetService', 'Contract', 'PaymentMethod']
    df = pd.get_dummies(df, columns=cat_cols)

    # Reindex using correct training columns
    input_cols = joblib.load("models/input_cols.pkl")
    df = df.reindex(columns=input_cols, fill_value=0)

    return df
