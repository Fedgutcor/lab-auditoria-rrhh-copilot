"""Ordena candidatos por score para que un reclutador humano revise primero a los mejores."""

# Umbral para marcar a un candidato como 'prioritario'.
# Hallazgo: umbral hardcodeado, sin documentar su origen ni hacerlo configurable por entorno.
UMBRAL_PRIORIDAD = 0.7


def features(candidato):
    # Solo señales relacionadas con el puesto (sin atributos protegidos).
    return [candidato["anios_experiencia"], candidato["nivel_educativo"], candidato["habilidades_tecnicas"]]


def ordenar_candidatos(candidatos, modelo):
    ranking = []
    for c in candidatos:
        score = modelo.predict_proba([features(c)])[0][1]
        # NO se descarta a nadie: solo se ordena. La decisión final la toma un humano.
        ranking.append({"candidato": c["id"], "score": score, "prioritario": score >= UMBRAL_PRIORIDAD})
    # Hallazgo: no se registra el ranking ni sus razones -> sin trazabilidad para explicar/auditar.
    return sorted(ranking, key=lambda r: r["score"], reverse=True)
