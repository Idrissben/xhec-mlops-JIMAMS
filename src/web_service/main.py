from app_config import APP_DESCRIPTION, APP_TITLE, MODEL_PATH
from fastapi import FastAPI
from lib.inference import batch_predict_workflow
from lib.models import DataInput
from utils import load_pickle

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION)

global_trained_model = load_pickle(MODEL_PATH)


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict")
def predict(payload: DataInput) -> dict:
    model = global_trained_model
    return {"prediction": batch_predict_workflow(payload.dict(), model=model)}
