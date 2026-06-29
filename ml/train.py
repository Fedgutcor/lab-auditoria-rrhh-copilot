"""Entrena el modelo que prioriza candidatos."""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def entrenar():
    # Hallazgo: el modelo se entrena con el historial de contrataciones de la empresa.
    # Si ese historial tiene sesgo de genero, el modelo lo aprende y lo amplifica
    # (caso Amazon 2018: su reclutador de IA penalizaba hojas de vida con la palabra 'women's').
    df = pd.read_csv("data/contrataciones_historicas.csv")
    y = df["fue_contratado"]
    X = df.drop(columns=["fue_contratado"])  # incluye genero, edad y universidad como features
    modelo = RandomForestClassifier()
    modelo.fit(X, y)
    return modelo
