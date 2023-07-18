# fast api script for deployment

## 1. imports packages
import uvicorn
from fastapi import FastAPI

from BankNote import BankNote
import numpy as np
import pandas as pd
import pickle 

## 2. Create the app object & ML model
app = FastAPI()

with open("classifier.pkl", "rb") as file:
    model = pickle.load(file)


## 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World!'}

## 4. Route with single parameter, returns the parameter within a message located at http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome here to learn ML models deployment': f'{name}'}

## 5. Expose the prediction func. make a prediction from the passed in simulated JSON data and return the Bank Note class prediction (0 or 1)
@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    print(data)

    # input data features
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    pred = classifier.predict([[variance, skewness, curtosis, entropy]])
    print('prediction: ',pred)
    if pred[0]>0.5:
        pred_output = "Fake note"
    else:
        pred_output = "True note"

    return {
        'prediction': pred_output
    }


## 6. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port=8000)

# uvicorn app:app --reload