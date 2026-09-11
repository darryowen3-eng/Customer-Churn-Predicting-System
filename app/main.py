from fastapi import FastAPI
import pandas as pd



from app.model import pipeline, threshold, explainer
from app.schemas import Client, ModelResponse


app=FastAPI()

@app.get("/")

def home():
    return {
        "Massage":"Skull gets hot so I am not nice"
    }

@app.post("/predict", response_model=ModelResponse)

def predict(client: Client):
    data = client.model_dump()
    
    data_input = pd.DataFrame([data])
    
    probability = pipeline.predict_proba(data_input)[0][1]
    
    prediction = 1 if probability>=threshold else 0
    
    
    preprocessed_data = pipeline[:-1].transform(data_input)
    
    shap_vals = explainer(data_input)[..., prediction].values
    
    return {
        "prediction": prediction,
        "probability": probability,
        "shap_values": shap_vals[0].tolist()
    }

