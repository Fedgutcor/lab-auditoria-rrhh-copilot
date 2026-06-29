from services.ranking import ordenar_candidatos, UMBRAL_PRIORIDAD


class ModeloFake:
    def predict_proba(self, X):
        # Score determinístico para la prueba.
        return [[0.2, 0.8]]


def test_ordena_y_marca_prioritario():
    candidatos = [{"id": 1, "anios_experiencia": 5, "nivel_educativo": 3, "habilidades_tecnicas": 4}]
    r = ordenar_candidatos(candidatos, ModeloFake())
    assert r[0]["candidato"] == 1
    assert r[0]["prioritario"] is True
    assert UMBRAL_PRIORIDAD == 0.7
