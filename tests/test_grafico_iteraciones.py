# pyrefly: ignore [missing-import]

import csv
import pytest

from src.scripts.grafico_iteraciones import generar_grafico_iteraciones


def test_grafico_iteraciones(tmp_path):
    archivo_csv = tmp_path / "resumen.csv"

    datos = [
        ["polinomica", "biseccion", 20, True],
        ["polinomica", "newton_raphson", 3, True],
        ["raiz_doble", "biseccion", 0, False],
        ["raiz_doble", "newton_mejorado", 1, True]
    ]

    with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow([
            "funcion", "metodo", "iteraciones", "convergio"
        ])

        for fila in datos:
            escritor.writerow(fila)

    grafico = generar_grafico_iteraciones(
        archivo_csv,
        tmp_path / "graficos"
    )

    assert grafico.exists()
    assert grafico.stat().st_size > 0


def test_csv_inexistente(tmp_path):
    with pytest.raises(FileNotFoundError):
        generar_grafico_iteraciones(
            tmp_path / "no_existe.csv",
            tmp_path / "graficos"
        )
