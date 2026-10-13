
from src.scripts.metodo_secante import secante


def test_secante_converge():
    f = lambda x: x**3 - x - 2

    resultado = secante(f, 1, 2)

    assert resultado["convergio"]
    assert abs(f(resultado["raiz"])) < 1e-6
    assert resultado["iteraciones"] <= 100


def test_secante_denominador_cero():
    f = lambda x: x**2 + 1

    resultado = secante(f, -1, 1)

    assert not resultado["convergio"]
