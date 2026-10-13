
from pathlib import Path

from src.scripts.funciones_prueba import funciones
from src.scripts.metodos_intervalo import biseccion, falsa_posicion
from src.scripts.metodo_punto_fijo import punto_fijo
from src.scripts.metodo_secante import secante
from src.scripts.metodos_newton import newton_raphson, newton_mejorado
from src.scripts.guardar_csv import guardar_datos, guardar_resumen


def ejecutar_experimentos(carpeta="src/data"):
    resultados = []
    tol = 1e-6
    max_iter = 100

    metodos = [
        "biseccion",
        "falsa_posicion",
        "punto_fijo",
        "secante",
        "newton_raphson",
        "newton_mejorado"
    ]

    for nombre, datos in funciones.items():
        f = datos["f"]
        a = datos["a"]
        b = datos["b"]
        p0 = datos["p0"]
        p1 = datos["p1"]

        guardar_datos(nombre, f, a, b, carpeta=carpeta)

        for metodo in metodos:
            try:
                if metodo == "biseccion":
                    resultado = biseccion(f, a, b, tol, max_iter)

                elif metodo == "falsa_posicion":
                    resultado = falsa_posicion(f, a, b, tol, max_iter)

                elif metodo == "punto_fijo":
                    resultado = punto_fijo(
                        f, datos["g"], p0, tol, max_iter
                    )

                elif metodo == "secante":
                    resultado = secante(f, p0, p1, tol, max_iter)

                elif metodo == "newton_raphson":
                    resultado = newton_raphson(
                        f, datos["df"], p0, tol, max_iter
                    )

                else:
                    resultado = newton_mejorado(
                        f, datos["df"], datos["d2f"],
                        p0, tol, max_iter
                    )

            except (ValueError, ZeroDivisionError, OverflowError):
                resultado = {
                    "raiz": None,
                    "iteraciones": 0,
                    "error": None,
                    "convergio": False,
                    "historial": []
                }

            fila = {
                "funcion": nombre,
                "metodo": metodo,
                "raiz": resultado["raiz"],
                "iteraciones": resultado["iteraciones"],
                "error": resultado["error"],
                "convergio": resultado["convergio"],
                "historial": resultado["historial"]
            }

            resultados.append(fila)

            print(
                nombre, "-", metodo,
                "- Convergio:", resultado["convergio"],
                "- Iteraciones:", resultado["iteraciones"]
            )

    archivo = Path(carpeta) / "resumen_metodos.csv"
    guardar_resumen(resultados, archivo)

    return resultados


if __name__ == "__main__":
    ejecutar_experimentos()
