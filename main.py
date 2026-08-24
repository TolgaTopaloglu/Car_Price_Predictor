import pandas as pd
from fastapi import FastAPI, Request
import pickle
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app= FastAPI()

templates= Jinja2Templates(directory="templates")

with open("CarMarketRegression.pkl", "rb") as file:
    model= pickle.load(file)

class CarPricingFeatures(BaseModel):
    Make: str
    Model: str
    Year: int
    Fuel_Type: str
    Transmission: str
    Engine_Size: float
    Mileage: int
    Horsepower: float
    Torque: float
    Owners: int
    Accident_History: float
    Service_History: str
    Color: str
    Body_Type: str
    Drivetrain: str
    Fuel_Efficiency: float
    Location: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(features: CarPricingFeatures):

    input_data=pd.DataFrame([features.model_dump()])

    prediction= model.predict(input_data)

    return {"prediction" : float(prediction[0])}