# Evaluación 2 - Búsqueda de raíces

**Laboratorio: La raíz que se esconde**  
**Asignatura:** Computación Numérica  
**Institución:** Universidad Católica del Maule  
**Profesor:** Juan Manuel Cabezas Contardo  
**Integrantes:** Kevin Villarroel y Rodrigo Retamal  
**Repositorio:** https://github.com/SadKeflon/evaluacion2-busqueda-raices

## Descripción

En este laboratorio implementamos seis métodos numéricos para encontrar raíces de ecuaciones de la forma `f(x) = 0`. Aplicamos cada método a funciones de distintos tipos y comparamos las aproximaciones obtenidas, el número de iteraciones y el comportamiento del error.

También estudiamos una función con raíz doble, donde la curva toca el eje x sin cruzarlo. Este caso permite observar por qué algunos métodos no se pueden aplicar y cómo cambia la convergencia de los demás.

## Métodos numéricos

| Método | Descripción | Archivo |
|---|---|---|
| Bisección | Reduce un intervalo que presenta cambio de signo. | `src/scripts/metodos_intervalo.py` |
| Falsa posición | Usa la intersección de una recta secante con el eje x y mantiene un intervalo con cambio de signo. | `src/scripts/metodos_intervalo.py` |
| Punto fijo | Construye aproximaciones sucesivas mediante `x = g(x)`. | `src/scripts/metodo_punto_fijo.py` |
| Secante | Calcula una nueva aproximación a partir de dos puntos, sin utilizar derivadas. | `src/scripts/metodo_secante.py` |
| Newton-Raphson | Utiliza la función y su primera derivada. | `src/scripts/metodos_newton.py` |
| Newton-Raphson mejorado | Utiliza la primera y segunda derivada para calcular la siguiente aproximación. | `src/scripts/metodos_newton.py` |

Para Newton-Raphson mejorado utilizamos la expresión vista en clases:

$$
x_{n+1}=x_n-\frac{f(x_n)f'(x_n)}{[f'(x_n)]^2-f(x_n)f''(x_n)}
$$

Cada método entrega la raíz aproximada, las iteraciones realizadas, el error estimado, un indicador de convergencia y el historial de las aproximaciones.

## Funciones de prueba

Las funciones se definen en `src/scripts/funciones_prueba.py`, junto con sus derivadas, intervalos y valores iniciales.

| Tipo | Función | Intervalo | Valores iniciales |
|---|---|---|---|
| Polinómica | `f(x) = x³ - x - 2` | `[1, 2]` | `p0 = 1.5`, `p1 = 2.0` |
| Polinómica con raíz doble | `f(x) = (x - 2)²` | `[1, 3]` | `p0 = 1.2`, `p1 = 2.5` |
| Logarítmica | `f(x) = ln(x) + x - 4` | `[2, 3]` | `p0 = 2.5`, `p1 = 3.0` |
| Exponencial | `f(x) = e^(-x) - x` | `[0, 1]` | `p0 = 0.5`, `p1 = 1.0` |
| Trigonométrica | `f(x) = cos(x) - x` | `[0, 1]` | `p0 = 0.5`, `p1 = 1.0` |
| Mixta | `f(x) = √x - cos(x)` | `[0.1, 1]` | `p0 = 0.5`, `p1 = 1.0` |

### Ambiente controlado

En los experimentos utilizamos las mismas condiciones generales:

- **Tolerancia:** `1e-6`.
- **Máximo de iteraciones:** `100`.
- **Intervalos y aproximaciones iniciales:** los indicados en la tabla anterior.
- **Funciones de punto fijo:** definidas como `g(x)` para cada caso en `funciones_prueba.py`.

En las cinco funciones con raíz simple se verifica un cambio de signo entre los extremos del intervalo, es decir, `f(a) * f(b) < 0`. Por continuidad, esto permite justificar la existencia de una raíz dentro del intervalo.

Para la función `f(x) = (x - 2)²` se cumple que `f(2) = 0` y `f'(2) = 0`. La raíz es `x = 2`, pero la función no cambia de signo. Por esta razón, bisección y falsa posición no pueden aplicarse con el intervalo indicado.

## Estructura del repositorio

```text
evaluacion2-busqueda-raices/
├── README.md
├── requirements.txt
├── informe.md
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
│   │   └── grafico_iteraciones.py
│   ├── data/
│   └── assets/
└── tests/
```

La carpeta `src/data` contiene los archivos CSV y `src/assets` contiene los gráficos PNG. En `tests` están las pruebas automáticas escritas con Pytest.

### Función de los scripts

| Script | Uso |
|---|---|
| `funciones_prueba.py` | Define las funciones, derivadas, intervalos y estimaciones iniciales. |
| `metodos_intervalo.py` | Implementa bisección y falsa posición. |
| `metodo_punto_fijo.py` | Implementa la iteración de punto fijo. |
| `metodo_secante.py` | Implementa secante. |
| `metodos_newton.py` | Implementa Newton-Raphson y Newton-Raphson mejorado. |
| `guardar_csv.py` | Guarda las muestras de las funciones y el resumen de resultados en CSV. |
| `experimentos.py` | Ejecuta los seis métodos sobre las seis funciones y reúne los resultados. |
| `graficos_funciones.py` | Genera los gráficos de las funciones con sus raíces marcadas. |
| `graficos_convergencia.py` | Grafica el error por iteración para comparar los métodos. |
| `grafico_iteraciones.py` | Genera el gráfico comparativo de iteraciones a partir del CSV resumen. |

## Requisitos e instalación

El proyecto se desarrolló con **Python 3.13.16**. Las bibliotecas utilizadas son NumPy, Matplotlib y Pytest, incluidas en `requirements.txt`.

Los siguientes comandos están pensados para **Windows PowerShell**.

Primero, clonar el repositorio:

```powershell
git clone https://github.com/SadKeflon/evaluacion2-busqueda-raices.git
cd evaluacion2-busqueda-raices
```

Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación del entorno, se puede habilitar temporalmente la ejecución de scripts en esa terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

El entorno virtual permite instalar las bibliotecas necesarias sin modificar las de otros proyectos de Python.

## Ejecución

Los comandos deben ejecutarse desde la carpeta principal del repositorio, con el entorno virtual activado.

### 1. Ejecutar los métodos y generar los CSV

```powershell
python -m src.scripts.experimentos
```

Se ejecutan las seis funciones con los seis métodos, para un total de **36 combinaciones**. Los casos donde un método no converge o no es aplicable se registran como tales.

El programa genera en `src/data` un archivo CSV por función:

```text
polinomica.csv
raiz_doble.csv
logaritmica.csv
exponencial.csv
trigonometrica.csv
mixta.csv
```

Cada uno contiene las columnas `x` y `f(x)`. También se genera `resumen_metodos.csv`, con las columnas `funcion`, `metodo`, `raiz`, `iteraciones`, `error` y `convergio`.

### 2. Graficar las funciones

```powershell
python -m src.scripts.graficos_funciones
```

Se guarda un gráfico PNG por función en `src/assets`, con la raíz aproximada marcada. El gráfico de la raíz doble permite observar que la curva toca el eje horizontal sin cruzarlo.

### 3. Graficar la convergencia

```powershell
python -m src.scripts.graficos_convergencia
```

Se generan seis gráficos que representan `log10(error)` frente al número de iteración. El error registrado por los métodos corresponde generalmente a la diferencia entre aproximaciones consecutivas, por lo que no siempre es el error verdadero respecto de la raíz.

### 4. Comparar las iteraciones

```powershell
python -m src.scripts.grafico_iteraciones
```

Este programa utiliza `src/data/resumen_metodos.csv` y genera `src/assets/comparacion_iteraciones.png`. Los casos señalados como `NC` corresponden a métodos que no convergieron o no pudieron aplicarse.

Si se quieren generar todos los resultados nuevamente, los cuatro comandos se ejecutan en el orden anterior.

## Pruebas

Las pruebas se encuentran en la carpeta `tests`. Para ejecutarlas todas:

```powershell
python -m pytest -v
```

También se puede ejecutar un archivo específico, por ejemplo:

```powershell
python -m pytest tests/test_biseccion.py -v
```

Las pruebas verifican el comportamiento de los métodos numéricos, algunos casos donde no pueden continuar y la generación de CSV y gráficos.

## Trabajo en GitHub

El repositorio utiliza tres ramas:

- `main`: contiene el código integrado para la evaluación.
- `kevin-villarroel`: rama de trabajo de Kevin.
- `rodrigo-retamal`: rama de trabajo de Rodrigo.

Cada integrante desarrolla y prueba sus cambios en su rama. Después se realizan commits, se publican los cambios y se integran a `main` mediante Pull Requests.

## Resultados e informe

Los resultados numéricos se almacenan en `src/data` y los gráficos en `src/assets`. Estos archivos permiten comparar la cantidad de iteraciones, el comportamiento del error y las situaciones en las que cada método encuentra dificultades.

El análisis de convergencia y las conclusiones del laboratorio se presentan en `informe.md`, donde se responden las preguntas de la evaluación utilizando los datos y gráficos obtenidos.
