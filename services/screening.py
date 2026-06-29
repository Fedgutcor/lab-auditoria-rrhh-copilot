"""Filtro automatico de hojas de vida."""
import requests
import os

THIRD_PARTY_API = "https://api.proveedor-externo.example/score"


def evaluar_candidato(hoja_de_vida: dict) -> dict:
    # Hallazgo: datos personales (hoja de vida) enviados a una API de terceros
    # sin base legal, sin acuerdo de tratamiento (DPA) y sin aviso al candidato.
    resp = requests.post(THIRD_PARTY_API, json=hoja_de_vida, timeout=10)
    score = resp.json().get("score", 0)

    decision = "avanza" if score >= 0.7 else "descartado"

    # Hallazgo: el descarte no registra la razon ni ofrece revision humana.
    if decision == "descartado":
        return {"decision": "descartado"}

    # Hallazgo: no hay 'humano en el circuito' obligatorio antes de una decision de alto impacto.
    return {"decision": decision, "score": score}
