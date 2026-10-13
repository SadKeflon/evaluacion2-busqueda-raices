
import csv

from src.scripts.experimentos import ejecutar_experimentos


def test_cantidad_resultados(tmp_path):
    resultados = ejecutar_experimentos(tmp_path)

    assert len(resultados) == 36


def test_archivos_csv(tmp_path):
    ejecutar_experimentos(tmp_path)

    archivos = list(tmp_path.glob("*.csv"))

    assert len(archivos) == 7
    assert (tmp_path / "resumen_metodos.csv").exists()


def test_resumen_csv(tmp_path):
    ejecutar_experimentos(tmp_path)

    archivo = tmp_path / "resumen_metodos.csv"

    with open(archivo, newline="", encoding="utf-8") as datos:
        filas = list(csv.DictReader(datos))

    assert len(filas) == 36


def test_raiz_doble_sin_cambio_signo(tmp_path):
    resultados = ejecutar_experimentos(tmp_path)

    for resultado in resultados:
        if resultado["funcion"] == "raiz_doble":
            if resultado["metodo"] in ["biseccion", "falsa_posicion"]:
                assert not resultado["convergio"]
