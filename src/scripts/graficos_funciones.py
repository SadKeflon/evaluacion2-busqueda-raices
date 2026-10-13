
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from src.scripts.funciones_prueba import funciones
from src.scripts.metodos_newton import newton_raphson, newton_mejorado


def generar_graficos(carpeta="src/assets"):
    carpeta = Path(carpeta)
    carpeta.mkdir(parents=True, exist_ok=True)

    archivos = []

    for nombre, datos in funciones.items():
        f = datos["f"]
        a = datos["a"]
        b = datos["b"]

        x = np.linspace(a, b, 300)
        y = f(x)

        if nombre == "raiz_doble":
            resultado = newton_mejorado(
                f, datos["df"], datos["d2f"], datos["p0"]
            )
        else:
            resultado = newton_raphson(
                f, datos["df"], datos["p0"]
            )

        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label="f(x)")
        plt.axhline(0, color="black", linewidth=0.8)

        if resultado["convergio"]:
            raiz = resultado["raiz"]

            plt.scatter(
                raiz, f(raiz),
                color="red",
                s=60,
                label="Raiz aproximada"
            )

        plt.title("Funcion " + nombre.replace("_", " "))
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()

        archivo = carpeta / (nombre + ".png")

        plt.savefig(archivo, dpi=150, bbox_inches="tight")
        plt.close()

        archivos.append(archivo)
        print("Grafico guardado:", archivo)

    return archivos


if __name__ == "__main__":
    generar_graficos()
