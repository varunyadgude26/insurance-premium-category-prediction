from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from model.prediction import model
from model.prediction import prediction
from schemas.user_data import UserData
import pandas as pd

app = FastAPI()

@app.get('/')
def home_page():
    return JSONResponse(status_code=200,content={'message':'API ENDPOINTS ARE ACTIVE'})

@app.get('/health')
def health_check():
    return {'status':'OK','model_loaded':model is not None}

@app.post('/predict')
def predict_response(data:UserData):
    try:

        # our prediction model needs only the computed field from the UserData,
        # but the UserData provides us with all the information so before passing
        # to the prediction model we need to fetch all the important fields from the UserData
        user_data = pd.DataFrame([{
            'bmi':data.bmi,
            'age_group':data.age_group,
            'life_risk' : data.life_risk,
            'city_tier':data.city_tier,
            'income_lpa':data.income_lpa,
            'occupation':data.occupation
            }])

        response = prediction(user_data)
        return JSONResponse(status_code=200,content = {"insurance_premium_category":response})
        
    except Exception as e:
        print(e)
