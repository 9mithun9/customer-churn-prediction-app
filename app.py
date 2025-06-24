from fastapi import FastAPI, HTTPException
from schema.customer_data import CustomerData
from models.predict import MODEL_VERSION, model, preprocess

app = FastAPI()


@app.get("/")
def home():
    return {'message': 'Customer Churn Prediction Model'}

@app.get("/health")
def health_check():
    return {
        'status' : 'OK',
        'version' : MODEL_VERSION,
        'model_load': model is not None
    }

@app.post("/predict")
def churn_prediction(data: CustomerData):


    try:
        x = preprocess(data)
        prediction = model.predict(x)[0][0]
        result = "Churn" if prediction > 0.5 else "No Churn"
        return {
            "Prediction" : result,
            "Probability" : float(prediction)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
