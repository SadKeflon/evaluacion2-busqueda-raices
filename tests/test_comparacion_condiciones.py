
import csv
from src.scripts.comparacion_condiciones import comparar_condiciones


def test_cantidad_comparaciones(tmp_path):
    archivo = tmp_path / "comparacion.csv"

    resultados = comparar_condiciones(archivo)

    assert len(resultados) == 9
    assert archivo.exists()


def test_resultados_convergen(tmp_path):
    archivo = tmp_path / "comparacion.csv"

    comparar_condiciones(archivo)

    with open(archivo, newline="", encoding="utf-8") as datos:
        filas = list(csv.DictReader(datos))

    for fila in filas:
        assert fila["convergio"] == "True"
        assert float(fila["residuo"]) < 1e-6
