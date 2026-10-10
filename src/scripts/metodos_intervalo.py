
import numpy as np


def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if a >= b or tol <= 0 or max_iter < 1:
        raise ValueError("Parametros iniciales invalidos")

    fa = float(f(a))
    fb = float(f(b))

    if not np.isfinite(fa) or not np.isfinite(fb):
        raise ValueError("La funcion no esta definida en los extremos")

    historial = []

    if abs(fa) < tol:
        return {
            "raiz": float(a),
            "iteraciones": 0,
            "error": 0.0,
            "convergio": True,
            "historial": historial
        }

    if abs(fb) < tol:
        return {
            "raiz": float(b),
            "iteraciones": 0,
            "error": 0.0,
            "convergio": True,
            "historial": historial
        }

    if fa * fb > 0:
        raise ValueError("El intervalo no presenta cambio de signo")

    anterior = None

    for n in range(1, max_iter + 1):
        x = (a + b) / 2
        fx = float(f(x))

        if not np.isfinite(fx):
            raise ValueError("Evaluacion no valida")

        error = (
            abs(b - a) / 2
            if anterior is None
            else abs(x - anterior)
        )

        historial.append({
            "iteracion": n,
            "x": float(x),
            "fx": fx,
            "error": float(error)
        })

        if abs(fx) < tol:
            return {
                "raiz": float(x),
                "iteraciones": n,
                "error": float(error),
                "convergio": True,
                "historial": historial
            }

        if fa * fx < 0:
            b = x
        else:
            a = x
            fa = fx

        anterior = x

    return {
        "raiz": float(x),
        "iteraciones": max_iter,
        "error": float(error),
        "convergio": False,
        "historial": historial
    }