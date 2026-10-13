
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from src.scripts.experimentos import ejecutar_experimentos


def generar_convergencia(carpeta="src/assets",
                        carpeta_datos="src/data"):
    carpeta = Path(carpeta)
    carpeta.mkdir(parents=True, exist_ok=True)

    resultados = ejecutar_experimentos(carpeta_datos)
    archivos = []

    funciones = []

    for resultado in resultados:
        nombre = resultado["funcion"]

        if nombre not in funciones:
            funciones.append(nombre)

    for nombre in funciones:
        plt.figure(figsize=(9, 5))
        hay_datos = False

        for resultado in resultados:
            if resultado["funcion"] != nombre:
                continue

            iteraciones = []
            errores = []

            for paso in resultado["historial"]:
                error = paso["error"]

                if np.isfinite(error) and error > 0:
                    iteraciones.append(paso["iteracion"])
                    errores.append(np.log10(error))

            if len(errores) > 0:
                plt.plot(
                    iteraciones,
                    errores,
                    marker=".",
                    label=resultado["metodo"]
                )
                hay_datos = True

        plt.title("Convergencia - " + nombre)
        plt.xlabel("Iteracion")
        plt.ylabel("log10(error)")
        plt.grid(True)

        if hay_datos:
            plt.legend()
        else:
            plt.text(
                0.5, 0.5,
                "Sin datos de convergencia",
                ha="center",
                transform=plt.gca().transAxes
            )

        archivo = carpeta / ("convergencia_" + nombre + ".png")

        plt.savefig(archivo, dpi=150, bbox_inches="tight")
        plt.close()

        archivos.append(archivo)
        print("Grafico guardado:", archivo)

    return archivos


if __name__ == "__main__":
    generar_convergencia()
