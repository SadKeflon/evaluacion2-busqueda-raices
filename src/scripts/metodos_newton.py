
import numpy as np


def newton_raphson(f, df, p0, tol=1e-6, max_iter=100):
    historial = []
    p0 = float(p0)

    for n in range(1, max_iter + 1):
        fp0 = float(f(p0))
        dfp0 = float(df(p0))

        if abs(fp0) < tol:
            return {
                "raiz": p0,
                "iteraciones": n - 1,
                "error": 0.0,
                "convergio": True,
                "historial": historial
            }

        if not np.isfinite(fp0) or not np.isfinite(dfp0):
            break

        if abs(dfp0) < 1e-12:
            break

        p = p0 - fp0 / dfp0

        if not np.isfinite(p):
            break

        fp = float(f(p))
        error = abs(p - p0)

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

        p0 = p

    return {
        "raiz": p0,
        "iteraciones": len(historial),
        "error": historial[-1]["error"] if historial else float("inf"),
        "convergio": False,
        "historial": historial
    }
