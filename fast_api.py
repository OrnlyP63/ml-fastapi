from fastapi import FastAPI
from pydantic import BaseModel
from model_prediction import prediction
from typing import List



class User_input(BaseModel):
    data_array: List


app = FastAPI()

@app.post("/predict")
def model(input:User_input):
    result = prediction(input.data_array)
    return result