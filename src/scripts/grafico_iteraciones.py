
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def generar_grafico_iteraciones(
    archivo_csv="src/data/resumen_metodos.csv",
    carpeta="src/assets"
):
    archivo_csv = Path(archivo_csv)

    if not archivo_csv.exists():
        raise FileNotFoundError(
            "Primero debes generar resumen_metodos.csv"
        )

    with open(archivo_csv, newline="", encoding="utf-8") as archivo:
        resultados = list(csv.DictReader(archivo))

    funciones = []
    metodos = []

    for resultado in resultados:
        nombre = resultado["funcion"]
        metodo = resultado["metodo"]

        if nombre not in funciones:
            funciones.append(nombre)

        if metodo not in metodos:
            metodos.append(metodo)

    x = np.arange(len(funciones))
    ancho = 0.12

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, metodo in enumerate(metodos):
        iteraciones = []
        convergencias = []

        for nombre in funciones:
            cantidad = 0
            convergio = False

            for resultado in resultados:
                if (resultado["funcion"] == nombre
                        and resultado["metodo"] == metodo):
                    convergio = resultado["convergio"] == "True"

                    if convergio:
                        cantidad = int(resultado["iteraciones"])

                    break

            iteraciones.append(cantidad)
            convergencias.append(convergio)

        posiciones = x + (i - (len(metodos) - 1)/2) * ancho

        ax.bar(
            posiciones,
            iteraciones,
            width=ancho,
            label=metodo
        )

        for j, convergio in enumerate(convergencias):
            if not convergio:
                ax.text(
                    posiciones[j],
                    0.5,
                    "NC",
                    ha="center",
                    va="bottom",
                    rotation=90,
                    fontsize=7
                )

    ax.set_title("Comparacion de iteraciones por metodo")
    ax.set_xlabel("Funcion")
    ax.set_ylabel("Cantidad de iteraciones")
    ax.set_xticks(x)
    ax.set_xticklabels(funciones, rotation=20)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    ax.text(
        0.01, -0.22,
        "NC: metodo que no convergio o no pudo aplicarse",
        transform=ax.transAxes,
        fontsize=9
    )

    carpeta = Path(carpeta)
    carpeta.mkdir(parents=True, exist_ok=True)

    archivo = carpeta / "comparacion_iteraciones.png"

    plt.savefig(archivo, dpi=150, bbox_inches="tight")
    plt.close()

    print("Grafico guardado:", archivo)

    return archivo


if __name__ == "__main__":
    generar_grafico_iteraciones()
