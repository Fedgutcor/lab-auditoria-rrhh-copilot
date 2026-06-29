"""Entrena el modelo que ORDENA candidatos (un reclutador humano decide)."""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Atributos protegidos: se excluyen del entrenamiento para evitar discriminación directa.
PROTEGIDOS = ["genero", "edad", "nombre", "foto"]


def entrenar(ruta_dataset):
    # El dataset vive FUERA del repo y está pseudonimizado (no hay PII en el código).
    df = pd.read_csv(ruta_dataset)
    y = df["fue_contratado"]
    X = df.drop(columns=["fue_contratado"] + PROTEGIDOS)
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X, y)
    # Hallazgo: el modelo se entrena con datos históricos pero NO se evalúa el sesgo
    # (sin test set ni métricas de equidad). Atributos proxy podrían reintroducir sesgo.
    return modelo
