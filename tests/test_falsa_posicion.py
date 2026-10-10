
import pytest
from src.scripts.metodos_intervalo import falsa_posicion


def test_falsa_posicion_converge():
    f = lambda x: x**3 - x - 2

    resultado = falsa_posicion(f, 1, 2)

    assert resultado["convergio"]
    assert abs(f(resultado["raiz"])) < 1e-6
    assert resultado["iteraciones"] <= 100


def test_falsa_posicion_sin_cambio_signo():
    f = lambda x: (x - 2)**2

    with pytest.raises(ValueError):
        falsa_posicion(f, 1, 3)
