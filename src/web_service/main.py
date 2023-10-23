from fastapi import FastAPI
from lib.models import DataInput
from lib.inference import batch_predict_workflow
from app_config import APP_TITLE, APP_DESCRIPTION, MODEL_PATH
from utils import load_pickle

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION)

global_trained_model = load_pickle(MODEL_PATH)

@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=DataInput, status_code=201)
def predict(payload: DataInput) -> dict:
    model = global_trained_model
    return {"prediction": batch_predict_workflow(payload.dict(),model=model)}
