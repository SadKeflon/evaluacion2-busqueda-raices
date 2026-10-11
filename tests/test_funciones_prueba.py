
import numpy as np
from src.scripts.funciones_prueba import funciones


def test_cantidad_funciones():
    assert len(funciones) == 6


def test_funciones_validas():
    for nombre, datos in funciones.items():
        f = datos["f"]
        x = datos["p0"]

        assert np.isfinite(f(x))
        assert np.isfinite(datos["df"](x))
        assert np.isfinite(datos["d2f"](x))


def test_cambio_de_signo():
    for nombre, datos in funciones.items():
        if nombre == "raiz_doble":
            continue

        f = datos["f"]
        a = datos["a"]
        b = datos["b"]

        assert f(a) * f(b) < 0


def test_raiz_doble():
    f = funciones["raiz_doble"]["f"]

    assert f(2) == 0
    assert f(1) > 0
    assert f(3) > 0
