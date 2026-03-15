from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import numpy as np
import pickle

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# load all models
models = pickle.load(open("all_models.pkl", "rb"))

# load encoders
encoders = pickle.load(open("label_encoder.pkl", "rb"))

le_sex = encoders["sex"]
le_smoker = encoders["smoker"]
le_region = encoders["region"]

# load best algorithm name
with open("best_model_name.txt") as f:
    best_algo = f.read()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "best_algo": best_algo
        }
    )


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    age: int = Form(...),
    sex: str = Form(...),
    bmi: float = Form(...),
    children: int = Form(...),
    smoker: str = Form(...),
    region: str = Form(...)
):

    sex = le_sex.transform([sex])[0]
    smoker = le_smoker.transform([smoker])[0]
    region = le_region.transform([region])[0]

    data = np.array([[age, sex, bmi, children, smoker, region]])

    predictions = {}

    for name, model in models.items():

        pred = model.predict(data)[0]

        predictions[name] = round(pred, 2)

    best_prediction = predictions[best_algo]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "predictions": predictions,
            "best_algo": best_algo,
            "best_prediction": best_prediction
        }
    )