# Evaluación 2 - Búsqueda de raíces

**Laboratorio:** La raíz que se esconde  
**Asignatura:** Computación Numérica  
**Institución:** Universidad Católica del Maule  
**Profesor:** Juan Manuel Cabezas Contardo  
**Integrantes:** Kevin Villarroel y Rodrigo Retamal  
**Repositorio:** https://github.com/SadKeflon/evaluacion2-busqueda-raices

## Descripción

En este laboratorio implementamos seis métodos numéricos para aproximar raíces de ecuaciones de la forma `f(x) = 0`. Los aplicamos a distintos tipos de funciones y comparamos las raíces obtenidas, las iteraciones necesarias y la evolución del error.

También trabajamos con una raíz doble, donde la gráfica toca el eje horizontal sin cruzarlo. Este caso permite estudiar por qué algunos métodos no se pueden aplicar con el intervalo elegido y por qué otros convergen más lentamente.

## Métodos numéricos

| Método | Descripción | Archivo |
|---|---|---|
| Bisección | Divide sucesivamente un intervalo donde hay cambio de signo. | `src/scripts/metodos_intervalo.py` |
| Falsa posición | Utiliza una recta secante para aproximar la raíz y mantiene el intervalo con cambio de signo. | `src/scripts/metodos_intervalo.py` |
| Punto fijo | Obtiene aproximaciones sucesivas mediante `x = g(x)`. | `src/scripts/metodo_punto_fijo.py` |
| Secante | Utiliza dos aproximaciones anteriores y no requiere derivadas. | `src/scripts/metodo_secante.py` |
| Newton-Raphson | Calcula nuevas aproximaciones utilizando la función y su primera derivada. | `src/scripts/metodos_newton.py` |
| Newton-Raphson mejorado | Utiliza la primera y segunda derivada para mejorar el comportamiento en raíces múltiples. | `src/scripts/metodos_newton.py` |

Para Newton-Raphson mejorado usamos la fórmula vista en clases:

$$
x_{n+1}=x_n-\frac{f(x_n)f'(x_n)}{[f'(x_n)]^2-f(x_n)f''(x_n)}
$$

Cada método devuelve la raíz aproximada, el número de iteraciones, un error estimado, el estado de convergencia y un historial de las iteraciones.

## Funciones de prueba

Las funciones se encuentran en `src/scripts/funciones_prueba.py`, junto con sus derivadas, intervalos y valores iniciales.

| Tipo | Función | Intervalo | Valores iniciales |
|---|---|---|---|
| Polinómica | `f(x) = x³ - x - 2` | `[1, 2]` | `p0 = 1.5`, `p1 = 2.0` |
| Polinómica con raíz doble | `f(x) = (x - 2)²` | `[1, 3]` | `p0 = 1.2`, `p1 = 2.5` |
| Logarítmica | `f(x) = ln(x) + x - 4` | `[2, 3]` | `p0 = 2.5`, `p1 = 3.0` |
| Exponencial | `f(x) = e^(-x) - x` | `[0, 1]` | `p0 = 0.5`, `p1 = 1.0` |
| Trigonométrica | `f(x) = cos(x) - x` | `[0, 1]` | `p0 = 0.5`, `p1 = 1.0` |
| Mixta | `f(x) = √x - cos(x)` | `[0.1, 1]` | `p0 = 0.5`, `p1 = 1.0` |

### Ambiente controlado

En los experimentos se utilizaron estas condiciones generales:

- **Tolerancia:** `1e-6`.
- **Máximo de iteraciones:** `100`.
- **Intervalos y aproximaciones iniciales:** los indicados en la tabla anterior.
- **Transformaciones de punto fijo:** las funciones `g(x)` definidas en `funciones_prueba.py`.

En las cinco funciones con raíces simples hay cambio de signo entre los extremos del intervalo, es decir, `f(a) * f(b) < 0`. Como las funciones son continuas en esos intervalos, esto permite justificar la existencia de al menos una raíz.

Para la raíz doble `f(x) = (x - 2)²`, se cumple que `f(2) = 0` y `f'(2) = 0`. La gráfica toca el eje horizontal en `x = 2`, pero no cambia de signo. Por eso, bisección y falsa posición no se pueden aplicar con el intervalo seleccionado.

## Estructura del repositorio

```text
evaluacion2-busqueda-raices/
├── .github/
│   └── workflows/
│       └── pruebas.yml
├── README.md
├── informe.md
├── requirements.txt
├── src/
│   ├── scripts/
│   │   ├── funciones_prueba.py
│   │   ├── metodos_intervalo.py
│   │   ├── metodo_punto_fijo.py
│   │   ├── metodo_secante.py
│   │   ├── metodos_newton.py
│   │   ├── guardar_csv.py
│   │   ├── experimentos.py
│   │   ├── graficos_funciones.py
│   │   ├── graficos_convergencia.py
│   │   ├── grafico_iteraciones.py
│   │   └── comparacion_condiciones.py
│   ├── data/
│   └── assets/
└── tests/
```

En `src/data` se guardan los archivos CSV, en `src/assets` los gráficos PNG y en `tests` las pruebas desarrolladas con Pytest.

### Función de los scripts

| Script | Uso |
|---|---|
| `funciones_prueba.py` | Define las funciones, derivadas, intervalos y estimaciones iniciales. |
| `metodos_intervalo.py` | Implementa bisección y falsa posición. |
| `metodo_punto_fijo.py` | Implementa la iteración de punto fijo. |
| `metodo_secante.py` | Implementa el método de la secante. |
| `metodos_newton.py` | Implementa Newton-Raphson y Newton-Raphson mejorado. |
| `guardar_csv.py` | Guarda los datos de las funciones y el resumen de resultados en CSV. |
| `experimentos.py` | Aplica los seis métodos a las seis funciones y reúne los resultados. |
| `graficos_funciones.py` | Genera las gráficas de las funciones con las raíces marcadas. |
| `graficos_convergencia.py` | Compara la evolución del error de los métodos por iteración. |
| `grafico_iteraciones.py` | Genera la comparación del número de iteraciones a partir del CSV resumen. |
| `comparacion_condiciones.py` | Compara bisección, Newton-Raphson y secante utilizando diferentes condiciones iniciales. |

## Requisitos e instalación

El proyecto se desarrolló con **Python 3.13.16** y utiliza **NumPy**, **Matplotlib** y **Pytest**, declarados en `requirements.txt`.

Los siguientes comandos están pensados para **Windows PowerShell**.

Primero, clonar el repositorio y entrar en su carpeta:

```powershell
git clone https://github.com/SadKeflon/evaluacion2-busqueda-raices.git
cd evaluacion2-busqueda-raices
```

Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación del entorno, se puede permitir temporalmente la ejecución de scripts en esa terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

## Ejecución

Todos los comandos se ejecutan desde la carpeta principal del repositorio, con el entorno virtual activado.

### 1. Ejecutar los métodos y generar los CSV

```powershell
python -m src.scripts.experimentos
```

Se prueban los seis métodos sobre las seis funciones, para un total de **36 combinaciones**. Los casos en que un método no converge o no se puede aplicar quedan identificados en los resultados.

En `src/data` se generan los siguientes archivos, con columnas `x` y `f(x)`:

```text
polinomica.csv
raiz_doble.csv
logaritmica.csv
exponencial.csv
trigonometrica.csv
mixta.csv
```

También se crea `resumen_metodos.csv`, con las columnas `funcion`, `metodo`, `raiz`, `iteraciones`, `error` y `convergio`.

### 2. Graficar las funciones

```powershell
python -m src.scripts.graficos_funciones
```

Se guarda un gráfico PNG por función en `src/assets`, con la raíz aproximada marcada. En la raíz doble se observa que la curva toca el eje horizontal sin cruzarlo.

### 3. Graficar la convergencia

```powershell
python -m src.scripts.graficos_convergencia
```

Se generan seis gráficos de `log10(error)` frente al número de iteración. En estos gráficos el error registrado corresponde principalmente al cambio entre aproximaciones consecutivas y no necesariamente al error verdadero de la raíz.

### 4. Comparar las iteraciones

```powershell
python -m src.scripts.grafico_iteraciones
```

Este programa utiliza `src/data/resumen_metodos.csv` y genera `src/assets/comparacion_iteraciones.png`. Los casos marcados como `NC` corresponden a métodos que no convergieron o no pudieron aplicarse.

### 5. Comparar condiciones iniciales

```powershell
python -m src.scripts.comparacion_condiciones
```

Este experimento realiza nueve pruebas adicionales con la función polinómica `f(x) = x³ - x - 2`. Se modifican los intervalos de bisección y las aproximaciones iniciales de Newton-Raphson y secante, manteniendo la misma tolerancia y el mismo límite de iteraciones.

Los resultados se guardan en `src/data/comparacion_condiciones.csv`, con el método, las condiciones iniciales, la raíz aproximada, las iteraciones, el estado de convergencia y el residuo final.

Para regenerar los resultados del laboratorio, se deben ejecutar los cinco comandos anteriores en ese orden.

## Pruebas

Las pruebas se encuentran en la carpeta `tests`. Para ejecutarlas todas:

```powershell
python -m pytest -v
```

También es posible probar un método por separado, por ejemplo:

```powershell
python -m pytest tests/test_biseccion.py -v
```

Las pruebas revisan casos de convergencia, algunas situaciones donde los métodos no pueden continuar y la generación de archivos CSV y gráficos.

El repositorio incluye el workflow `.github/workflows/pruebas.yml`, que está configurado para ejecutar Pytest mediante GitHub Actions cuando hay cambios en las ramas de trabajo o Pull Requests hacia `main`.

## Trabajo en GitHub

El repositorio utiliza tres ramas:

- `main`: contiene el trabajo integrado para la evaluación.
- `kevin-villarroel`: rama de desarrollo de Kevin.
- `rodrigo-retamal`: rama de desarrollo de Rodrigo.

Cada integrante trabaja y prueba sus cambios en su propia rama. Después se realizan commits y se integran los avances a `main` mediante Pull Requests.

## Resultados e informe

Los CSV se encuentran en `src/data` y los gráficos en `src/assets`. A partir de estos archivos se comparan las iteraciones y el comportamiento de los métodos.

En los 36 experimentos principales, 33 ejecuciones cumplieron el criterio de convergencia utilizado. Las otras tres corresponden a bisección y falsa posición en la raíz doble, donde no se puede aplicar el criterio de cambio de signo, y a punto fijo en esa misma función, que no alcanzó la tolerancia en 100 iteraciones.

El análisis detallado, la comparación de los órdenes de convergencia y las conclusiones están en `informe.md`, donde se responden las preguntas de la evaluación utilizando los datos y gráficos obtenidos.
