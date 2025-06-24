
# 📞 Customer Churn Prediction App

A machine learning-powered web application that predicts whether a telecom customer is likely to churn, using a logistic regression model trained on the Telco Customer Churn dataset.

<div align="center">
  <img src="https://img.shields.io/badge/Backend-FastAPI-green" />
  <img src="https://img.shields.io/badge/Frontend-Streamlit-red" />
  <img src="https://img.shields.io/badge/Deployed-AWS EC2-blue" />
  <img src="https://img.shields.io/badge/Dockerized-Yes-blueviolet" />
</div>

---

## 🔗 Live Links

- 🧠 **API Docs:** [http://13.204.79.251:8000/docs](http://13.204.79.251:8000/docs)
- 📦 **Docker Image:** [Docker Hub](https://hub.docker.com/r/mithunmarshal/customer-churn-prediction-model)
- 📊 **Dataset:** [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- 📈 **Power BI App:** [Open Dashboard](https://app.powerbi.com/Redirect?action=OpenApp&appId=76c1d8d4-234b-497c-93e1-41eca07c048d&ctid=e8fe393e-b0c7-4e81-addc-84295f3382c5&experience=power-bi)

---

## 🧠 Features

- Predicts customer churn using logistic regression
- REST API built with FastAPI
- Streamlit frontend interface
- Dockerized for easy deployment
- Hosted on AWS EC2 instance
- Power BI dashboard visualization
- Clean input validation using Pydantic schema

---

## ⚙️ Tech Stack

| Layer          | Tech                                  |
|----------------|----------------------------------------|
| Backend        | FastAPI, Uvicorn                      |
| Frontend       | Streamlit                             |
| ML Model       | **Neural Network** (Keras, TensorFlow) |
| Preprocessing  | MinMaxScaler, OneHotEncoding          |
| Deployment     | Docker, AWS EC2                       |
| Reporting      | Power BI                              |

---

## 📁 Folder Structure

```
customer-churn-prediction-app/
├── app.py
├── dockerfile
├── requirements.txt
├── streamlit.py
├── .gitignore
├── models/
│   └── predict.py
├── schema/
│   └── customer_data.py
├── image/
│   ├── streamlit-ui.png
│   └── customer-churn.jpg
```

---

## 🛠️ Local Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/9mithun9/customer-churn-prediction-app.git
cd customer-churn-prediction-app
```

### 2. Setup Virtual Environment

```bash
python -m venv myenv
myenv/Scripts/activate       # On Windows
# OR
source myenv/bin/activate    # On Mac/Linux

pip install -r requirements.txt
```

### 3. Start Backend (FastAPI)

```bash
uvicorn app:app --reload
# Visit: http://127.0.0.1:8000/docs
```

### 4. Start Frontend (Streamlit)

```bash
streamlit run streamlit.py
```

---

## 🐳 Docker Deployment

### 1. Pull the Image

```bash
docker pull mithunmarshal/customer-churn-prediction-model
```

### 2. Run the Container

```bash
docker run -p 8000:8000 mithunmarshal/customer-churn-prediction-model
```

---

## 🧪 Sample Input JSON

```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 80.5,
  "TotalCharges": 900.6
}
```

---

## 🧑‍💻 Streamlit Frontend

> The frontend is built using Streamlit, allowing users to input customer details and instantly receive a churn prediction.

<p align="center">
  <img src="image/streamlit-ui.png" width="600" />
</p>

---

## 📈 Power BI Report

> Scan the QR code below to view the interactive Power BI dashboard:

<p align="center">
  <img src="image/customer-churn.jpg" width="200" />
</p>

Or open directly here:  
🔗 [Power BI App](https://app.powerbi.com/Redirect?action=OpenApp&appId=76c1d8d4-234b-497c-93e1-41eca07c048d&ctid=e8fe393e-b0c7-4e81-addc-84295f3382c5&experience=power-bi)

---

## 🧾 Model & Notebook

- The model was trained using the [Telco Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Jupyter Notebook: `Telco_Customer_Churn_Prediction_Model.ipynb`
- Saved model, scaler, and column files are used during API prediction

---

## 🙌 Author

**Mithun Marshal**  
📂 GitHub: [@9mithun9](https://github.com/9mithun9)

---

## 📝 License

This project is open source and free to use under the MIT License.
