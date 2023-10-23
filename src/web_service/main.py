<<<<<<< HEAD
# Code with FastAPI (app = FastAPI(...))


from fastapi import FastAPI

# Other imports

app = FastAPI(title="...", description="...")
=======
from app_config import APP_DESCRIPTION, APP_TITLE, MODEL_PATH
from fastapi import FastAPI
from lib.inference import batch_predict_workflow
from lib.models import DataInput
from utils import load_pickle

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION)

global_trained_model = load_pickle(MODEL_PATH)
>>>>>>> 5b8ffe6fbd4e13fff896e532952e5b28df94cb18


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


<<<<<<< HEAD
@app.post("/predict", response_model="InsertHereAPydanticClass", status_code=201)
def predict(payload: "InsertHereAPydanticClass") -> dict:
    # TODO: complete and replace the "InsertHereAPydanticClass" with the correct Pydantic classes defined in web_service/lib/models.py
=======
@app.post("/predict")
def predict(payload: DataInput) -> dict:
    model = global_trained_model
    return {"prediction": batch_predict_workflow(payload.dict(), model=model)}
>>>>>>> 5b8ffe6fbd4e13fff896e532952e5b28df94cb18
