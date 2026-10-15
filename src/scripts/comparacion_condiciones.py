
import csv
from pathlib import Path

from src.scripts.metodos_intervalo import biseccion
from src.scripts.metodos_newton import newton_raphson
from src.scripts.metodo_secante import secante


def comparar_condiciones(archivo="src/data/comparacion_condiciones.csv"):
    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1

    tol = 1e-6
    max_iter = 100

    casos = [
        ("Biseccion", "[1, 2]",
         biseccion(f, 1, 2, tol, max_iter)),

        ("Biseccion", "[1.4, 1.6]",
         biseccion(f, 1.4, 1.6, tol, max_iter)),

        ("Biseccion", "[1.5, 1.55]",
         biseccion(f, 1.5, 1.55, tol, max_iter)),

        ("Newton-Raphson", "p0 = 1",
         newton_raphson(f, df, 1, tol, max_iter)),

        ("Newton-Raphson", "p0 = 1.5",
         newton_raphson(f, df, 1.5, tol, max_iter)),

        ("Newton-Raphson", "p0 = 2",
         newton_raphson(f, df, 2, tol, max_iter)),

        ("Secante", "p0 = 1, p1 = 2",
         secante(f, 1, 2, tol, max_iter)),

        ("Secante", "p0 = 1.4, p1 = 1.6",
         secante(f, 1.4, 1.6, tol, max_iter)),

        ("Secante", "p0 = 1.5, p1 = 1.6",
         secante(f, 1.5, 1.6, tol, max_iter))
    ]

    resultados = []

    for metodo, condiciones, resultado in casos:
        raiz = resultado["raiz"]

        fila = {
            "metodo": metodo,
            "condiciones": condiciones,
            "raiz": raiz,
            "iteraciones": resultado["iteraciones"],
            "convergio": resultado["convergio"],
            "residuo": abs(f(raiz))
        }

        resultados.append(fila)

        print(
            metodo, condiciones,
            "- Iteraciones:", resultado["iteraciones"]
        )

    archivo = Path(archivo)
    archivo.parent.mkdir(parents=True, exist_ok=True)

    with open(archivo, "w", newline="", encoding="utf-8") as datos:
        escritor = csv.DictWriter(
            datos,
            fieldnames=[
                "metodo", "condiciones", "raiz",
                "iteraciones", "convergio", "residuo"
            ]
        )

        escritor.writeheader()
        escritor.writerows(resultados)

    return resultados


if __name__ == "__main__":
    comparar_condiciones()
