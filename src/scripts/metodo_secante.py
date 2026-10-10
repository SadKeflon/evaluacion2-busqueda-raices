
import numpy as np


def secante(f, p0, p1, tol=1e-6, max_iter=100):
    historial = []
    p0 = float(p0)
    p1 = float(p1)

    f0 = float(f(p0))
    f1 = float(f(p1))

    if abs(f0) < tol:
        return {
            "raiz": p0,
            "iteraciones": 0,
            "error": 0.0,
            "convergio": True,
            "historial": historial
        }

    if abs(f1) < tol:
        return {
            "raiz": p1,
            "iteraciones": 0,
            "error": 0.0,
            "convergio": True,
            "historial": historial
        }

    error = float("inf")

    for n in range(1, max_iter + 1):
        denominador = f1 - f0

        if abs(denominador) < 1e-12:
            break

        p = p1 - f1 * (p1 - p0) / denominador

        if not np.isfinite(p):
            break

        fp = float(f(p))
        error = abs(p - p1)

        if not np.isfinite(fp):
            break

        historial.append({
            "iteracion": n,
            "x": p,
            "fx": fp,
            "error": error
        })

        if abs(fp) < tol:
            return {
                "raiz": p,
                "iteraciones": n,
                "error": error,
                "convergio": True,
                "historial": historial
            }

        p0 = p1
        f0 = f1

        p1 = p
        f1 = fp

    return {
        "raiz": p1,
        "iteraciones": len(historial),
        "error": error,
        "convergio": False,
        "historial": historial
    }
