from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
)
from pydantic import BaseModel
from fastapi import FastAPI
import tensorflow as tf
import joblib
import pandas as pd

class Iris(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
    
app = FastAPI(title="Iris ML API", description="API for iris dataset ml model", version="1.0")

model = tf.keras.models.load_model("../model/TF-Iris.h5")

def get_prediction(data):
    print(data)
    return 1

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
async def predict(params: Iris):
    print(params)
    pred = get_prediction(params)

    return pred