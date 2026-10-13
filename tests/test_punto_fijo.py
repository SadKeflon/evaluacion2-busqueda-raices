import numpy as np
from src.scripts.metodo_punto_fijo import punto_fijo


def test_punto_fijo_converge():
    f = lambda x: np.cos(x) - x
    g = lambda x: np.cos(x)

    resultado = punto_fijo(f, g, 0.5)

    assert resultado["convergio"]
    assert abs(f(resultado["raiz"])) < 1e-6
    assert resultado["iteraciones"] <= 100


def test_punto_fijo_no_converge():
    f = lambda x: x + 1
    g = lambda x: 2*x + 1

    resultado = punto_fijo(f, g, 0, max_iter=8)

    assert not resultado["convergio"]
    assert resultado["iteraciones"] == 8