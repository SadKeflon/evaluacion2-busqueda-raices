
import pytest
from src.scripts.metodos_intervalo import biseccion


def test_biseccion_converge():
    f = lambda x: x**3 - x - 2
    resultado = biseccion(f, 1, 2)

    assert resultado["convergio"]
    assert abs(f(resultado["raiz"])) < 1e-6
    assert resultado["iteraciones"] <= 100


def test_biseccion_sin_cambio_de_signo():
    f = lambda x: (x - 2)**2

    with pytest.raises(ValueError):
        biseccion(f, 1, 3)
