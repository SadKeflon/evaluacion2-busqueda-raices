
import csv
from src.scripts.guardar_csv import guardar_datos, guardar_resumen


def test_guardar_datos(tmp_path):
    f = lambda x: x**2 - 4

    archivo = guardar_datos(
        "ejemplo", f, 0, 3, cantidad=4, carpeta=tmp_path
    )

    assert archivo.exists()

    with open(archivo, newline="", encoding="utf-8") as datos:
        filas = list(csv.reader(datos))

    assert filas[0] == ["x", "f(x)"]
    assert len(filas) == 5
    assert float(filas[-1][1]) == 5.0


def test_guardar_resumen(tmp_path):
    resultados = [
        {
            "funcion": "polinomica",
            "metodo": "biseccion",
            "raiz": 1.52138,
            "iteraciones": 20,
            "error": 0.000001,
            "convergio": True
        }
    ]

    archivo = guardar_resumen(
        resultados, tmp_path / "resumen.csv"
    )

    assert archivo.exists()

    with open(archivo, newline="", encoding="utf-8") as datos:
        filas = list(csv.DictReader(datos))

    assert len(filas) == 1
    assert filas[0]["metodo"] == "biseccion"
    assert filas[0]["funcion"] == "polinomica"
