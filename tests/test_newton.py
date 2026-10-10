
from src.scripts.metodos_newton import newton_raphson


def test_newton_converge():
    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1

    resultado = newton_raphson(f, df, 1.5)

    assert resultado["convergio"]
    assert abs(f(resultado["raiz"])) < 1e-6
    assert resultado["iteraciones"] <= 100


def test_newton_derivada_cero():
    f = lambda x: x**2 + 1
    df = lambda x: 2*x

    resultado = newton_raphson(f, df, 0)

    assert not resultado["convergio"]
