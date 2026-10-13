import numpy as np


def punto_fijo(f, g, p0, tol=1e-6, max_iter=100):
    historial = []
    p0 = float(p0)

    for n in range(1, max_iter + 1):
        p = float(g(p0))

        if not np.isfinite(p):
            break

        error = abs(p - p0)
        fx = float(f(p))

        if not np.isfinite(fx):
            break

        historial.append({
            "iteracion": n,
            "x": p,
            "fx": fx,
            "error": error
        })

        if error < tol and abs(fx) < tol:
            return {
                "raiz": p,
                "iteraciones": n,
                "error": error,
                "convergio": True,
                "historial": historial
            }

        p0 = p

    return {
        "raiz": p0,
        "iteraciones": len(historial),
        "error": historial[-1]["error"] if historial else float("inf"),
        "convergio": False,
        "historial": historial
    }