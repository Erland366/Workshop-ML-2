from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
)
from pydantic import BaseModel
from fastapi import FastAPI
import tensorflow as tf
import joblib
import numpy as np

class Iris(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
    
app = FastAPI(title="Iris ML API", description="API for iris dataset ml model")

model = tf.keras.models.load_model("model/TF-Iris.h5")

def get_prediction(data):
    data_raw = data.dict()
    data_tensor = tf.constant(list(data_raw.values()), dtype=tf.float32)[None]
    predict = model.predict(data_tensor)
    return {"prediction" : float(np.argmax(predict))}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
async def predict(params: Iris):
    pred = get_prediction(params)

    return pred