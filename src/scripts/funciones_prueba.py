
import numpy as np


funciones = {
    "polinomica": {
        "f": lambda x: x**3 - x - 2,
        "df": lambda x: 3*x**2 - 1,
        "d2f": lambda x: 6*x,
        "g": lambda x: np.cbrt(x + 2),
        "a": 1.0,
        "b": 2.0,
        "p0": 1.5,
        "p1": 2.0
    },

    "raiz_doble": {
        "f": lambda x: (x - 2)**2,
        "df": lambda x: 2*(x - 2),
        "d2f": lambda x: 2,
        "g": lambda x: x + (x - 2)**2,
        "a": 1.0,
        "b": 3.0,
        "p0": 1.2,
        "p1": 2.5
    },

    "logaritmica": {
        "f": lambda x: np.log(x) + x - 4,
        "df": lambda x: 1/x + 1,
        "d2f": lambda x: -1/x**2,
        "g": lambda x: 4 - np.log(x),
        "a": 2.0,
        "b": 3.0,
        "p0": 2.5,
        "p1": 3.0
    },

    "exponencial": {
        "f": lambda x: np.exp(-x) - x,
        "df": lambda x: -np.exp(-x) - 1,
        "d2f": lambda x: np.exp(-x),
        "g": lambda x: np.exp(-x),
        "a": 0.0,
        "b": 1.0,
        "p0": 0.5,
        "p1": 1.0
    },

    "trigonometrica": {
        "f": lambda x: np.cos(x) - x,
        "df": lambda x: -np.sin(x) - 1,
        "d2f": lambda x: -np.cos(x),
        "g": lambda x: np.cos(x),
        "a": 0.0,
        "b": 1.0,
        "p0": 0.5,
        "p1": 1.0
    },

    "mixta": {
        "f": lambda x: np.sqrt(x) - np.cos(x),
        "df": lambda x: 1/(2*np.sqrt(x)) + np.sin(x),
        "d2f": lambda x: -1/(4*x**1.5) + np.cos(x),
        "g": lambda x: (x + np.cos(x)**2)/2,
        "a": 0.1,
        "b": 1.0,
        "p0": 0.5,
        "p1": 1.0
    }
}
