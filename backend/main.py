from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
from woe_transformer import WoETransformer


def prob_to_score(prob, base_point=600, pdo=50, odds=15):
    """
    Convierte una probabilidad en un puntaje de scorecard.
    base_point: Puntaje base (por ejemplo 600)
    pdo: Points to Double Odds (ej. 50 = cada 50 puntos se duplican las probabilidades)
    odds: Odds base en el puntaje base (ej. 15 significa 15:1 buenos/malos)
    """
    # Score formula: score = offset - factor * log(odds)
    factor = pdo / np.log(2)
    offset = base_point - factor * np.log(odds)
    odds_value = (1 - prob) / prob
    score = offset + factor * np.log(odds_value)
    return round(score, 0)

app = FastAPI()

model = joblib.load("fraud_model_pipeline.pkl")

# Declaring our FastAPI instance
app = FastAPI()
 
# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Fraud scorecard API'}

@app.post("/score")
def score(data: dict):
    """
    Recibe un diccionario con las variables del modelo.
    """
    # Convertir a DataFrame (1 fila)
    df = pd.DataFrame([data])

    # Probabilidad de fraude
    prob = model.predict_proba(df)[:, 1][0]

    # Calcular score
    score = prob_to_score(prob)

    return {
        "fraud_probability": round(prob, 4),
        "score": int(score)
    }