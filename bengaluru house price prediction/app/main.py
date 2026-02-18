import os
import json
import pickle
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.utils import predict_price
import numpy as np

app = FastAPI(title="Bengaluru Home Price Predictor")

# ---------------- Paths ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
MODEL_PATH = os.path.join(BASE_DIR, "models", "bengaluru_home_price_model.pickle")
COLUMNS_PATH = os.path.join(BASE_DIR, "..", "columns.json")  # columns.json at root

# ---------------- Mount Static ----------------
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

# ---------------- Load Model ----------------
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(COLUMNS_PATH, "r") as f:
    data_columns = json.load(f)["data_sources"]

# ---------------- Routes ----------------
@app.get("/")
def home(request: Request):
    locations = [col for col in data_columns if col not in ["total_sqft", "bath", "bhk"]]
    return templates.TemplateResponse("index.html", {"request": request, "locations": locations})


@app.post("/predict")
def predict(
    request: Request,
    location: str = Form(...),
    sqft: float = Form(...),
    bath: int = Form(...),
    bhk: int = Form(...)
):
    # Backend validation
    errors = []
    if not location or location.strip() == "":
        errors.append("Please select a location.")
    if sqft <= 0:
        errors.append("Enter valid square feet.")
    if bath <= 0:
        errors.append("Enter valid number of bathrooms.")
    if bhk <= 0:
        errors.append("Enter valid BHK.")

    if errors:
        predicted_price = "Error: " + " | ".join(errors)
    else:
        try:
            predicted_price = predict_price(location, sqft, bath, bhk, model, data_columns)
            predicted_price = round(predicted_price, 2)
        except Exception as e:
            predicted_price = f"Error: {str(e)}"

    locations = [col for col in data_columns if col not in ["total_sqft", "bath", "bhk"]]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "predicted_price": predicted_price,
        "locations": locations
    })
