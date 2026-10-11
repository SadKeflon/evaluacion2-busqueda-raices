
import csv
from pathlib import Path
import numpy as np


def guardar_datos(nombre, f, a, b, cantidad=201, carpeta="src/data"):
    carpeta = Path(carpeta)
    carpeta.mkdir(parents=True, exist_ok=True)

    archivo = carpeta / (nombre + ".csv")

    valores_x = np.linspace(a, b, cantidad)

    with open(archivo, "w", newline="", encoding="utf-8") as datos:
        escritor = csv.writer(datos)
        escritor.writerow(["x", "f(x)"])

        for x in valores_x:
            fx = f(x)
            escritor.writerow([float(x), float(fx)])

    return archivo


def guardar_resumen(resultados, archivo="src/data/resumen_metodos.csv"):
    archivo = Path(archivo)
    archivo.parent.mkdir(parents=True, exist_ok=True)

    columnas = [
        "funcion",
        "metodo",
        "raiz",
        "iteraciones",
        "error",
        "convergio"
    ]

    with open(archivo, "w", newline="", encoding="utf-8") as datos:
        escritor = csv.DictWriter(datos, fieldnames=columnas)
        escritor.writeheader()

        for resultado in resultados:
            escritor.writerow({
                "funcion": resultado["funcion"],
                "metodo": resultado["metodo"],
                "raiz": resultado["raiz"],
                "iteraciones": resultado["iteraciones"],
                "error": resultado["error"],
                "convergio": resultado["convergio"]
            })

    return archivo
