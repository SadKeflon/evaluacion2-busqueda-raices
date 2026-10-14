# Evaluación 2 - Búsqueda de raíces

**La raíz que se esconde: comparación de métodos numéricos y análisis de convergencia**

**Universidad:** Universidad Católica del Maule  
**Asignatura:** Computación Numérica  
**Actividad:** Laboratorio evaluado 2  
**Docente:** Juan Manuel Cabezas Contardo  
**Integrantes:** Kevin Villarroel y Rodrigo Retamal  
**Repositorio:** [SadKeflon/evaluacion2-busqueda-raices](https://github.com/SadKeflon/evaluacion2-busqueda-raices)

## 1. Descripción y objetivo

Este proyecto implementa seis métodos numéricos para aproximar soluciones de ecuaciones de la forma **f(x) = 0**. El objetivo no es solamente obtener una raíz, sino comparar el comportamiento de los métodos: cuántas iteraciones necesitan, cómo disminuye el error y en qué situaciones pueden fallar.

Se estudian seis funciones, entre ellas una **raíz doble** que toca el eje horizontal sin cruzarlo. Los experimentos generan archivos CSV, gráficos de las funciones, curvas de convergencia y una comparación del número de iteraciones.

## 2. Métodos implementados

| Método | Tipo | Característica principal | Archivo |
|---|---|---|---|
| Bisección | Cerrado | Divide repetidamente un intervalo con cambio de signo. | `src/scripts/metodos_intervalo.py` |
| Falsa posición | Cerrado | Aproxima la raíz con una recta secante, conservando un intervalo con cambio de signo. | `src/scripts/metodos_intervalo.py` |
| Punto fijo | Abierto | Itera a partir de una expresión `x = g(x)`; depende de la elección de `g`. | `src/scripts/metodo_punto_fijo.py` |
| Secante | Abierto | Utiliza dos estimaciones iniciales sin calcular derivadas. | `src/scripts/metodo_secante.py` |
| Newton-Raphson | Abierto | Utiliza la primera derivada para actualizar la aproximación. | `src/scripts/metodos_newton.py` |
| Newton-Raphson mejorado | Abierto | Utiliza la primera y segunda derivada; se estudia especialmente en la raíz doble. | `src/scripts/metodos_newton.py` |

El método de Newton-Raphson mejorado utiliza la expresión enseñada en clases:

```text
x_nuevo = x - f(x) * f'(x) / (f'(x)^2 - f(x) * f''(x))
```

Los métodos registran sus resultados con los campos `raiz`, `iteraciones`, `error`, `convergio` e `historial`. Cada elemento del historial contiene el número de iteración, la aproximación, el valor de la función y una estimación del error.

## 3. Funciones de prueba y ambiente controlado

Los experimentos utilizan **tolerancia de `1e-6`** y un **máximo de 100 iteraciones**. Cada función tiene un intervalo y estimaciones iniciales definidos en `src/scripts/funciones_prueba.py`.

| Caso | Función f(x) | Intervalo [a, b] | x0 | x1 |
|---|---|---|---:|---:|
| Polinómica | `x³ - x - 2` | `[1, 2]` | 1.5 | 2.0 |
| Raíz doble | `(x - 2)²` | `[1, 3]` | 1.2 | 2.5 |
| Logarítmica | `ln(x) + x - 4` | `[2, 3]` | 2.5 | 3.0 |
| Exponencial | `e^(-x) - x` | `[0, 1]` | 0.5 | 1.0 |
| Trigonométrica | `cos(x) - x` | `[0, 1]` | 0.5 | 1.0 |
| Mixta | `sqrt(x) - cos(x)` | `[0.1, 1]` | 0.5 | 1.0 |

El archivo de funciones incluye, además, las derivadas necesarias para Newton, la segunda derivada para Newton mejorado y una función `g(x)` para punto fijo.

### Comprobación de la existencia de raíces

Para las cinco funciones con raíz simple, los intervalos seleccionados cumplen **f(a) · f(b) < 0**. Como son continuas en esos intervalos, existe al menos una raíz entre sus extremos (teorema de Bolzano).

| Función | f(a), aproximado | f(b), aproximado | Condición |
|---|---:|---:|---|
| Polinómica | -2.0000 | 4.0000 | Cambio de signo |
| Logarítmica | -1.3069 | 0.0986 | Cambio de signo |
| Exponencial | 1.0000 | -0.6321 | Cambio de signo |
| Trigonométrica | 1.0000 | -0.4597 | Cambio de signo |
| Mixta | -0.6788 | 0.4597 | Cambio de signo |

En cambio, para `f(x) = (x - 2)²` se cumple `f(2) = 0` y `f'(2) = 0`, pero la función no cambia de signo a ambos lados de `x = 2`. Por eso bisección y falsa posición, con el intervalo propuesto, **no son aplicables**. Esta situación también se observa en el gráfico de la raíz doble.

Los valores iniciales y la elección de `g(x)` pueden influir en la convergencia. No se presupone que todos los métodos converjan para todas las funciones.

## 4. Estructura del proyecto

```text
evaluacion2-busqueda-raices/
├── README.md
├── requirements.txt
├── .gitignore
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
│   ├── data/                 # CSV generados
│   └── assets/               # Gráficos PNG generados
└── tests/                    # Pruebas con Pytest
```

Además, la entrega debe incluir `informe.md` en la raíz del repositorio. Las pruebas y los resultados se amplían conforme se integran las contribuciones de ambos integrantes a `main`.

### ¿Qué hace cada script?

| Script | Función |
|---|---|
| `funciones_prueba.py` | Define las seis funciones, sus derivadas, transformaciones para punto fijo, intervalos y estimaciones iniciales. |
| `metodos_intervalo.py` | Implementa bisección y falsa posición. |
| `metodo_punto_fijo.py` | Implementa la iteración de punto fijo. |
| `metodo_secante.py` | Implementa el método de la secante. |
| `metodos_newton.py` | Implementa Newton-Raphson y Newton-Raphson mejorado. |
| `guardar_csv.py` | Escribe los pares `(x, f(x))` de cada función y el resumen de los métodos en archivos CSV. |
| `experimentos.py` | Ejecuta los seis métodos para cada una de las seis funciones y prepara el resumen de resultados. |
| `graficos_funciones.py` | Grafica cada función y señala una raíz aproximada, cuando el método utilizado converge. |
| `graficos_convergencia.py` | Genera los gráficos de convergencia por función, comparando los historiales de los métodos. |
| `grafico_iteraciones.py` | Genera un gráfico de barras con las iteraciones por método y función a partir del CSV resumen. |

La carpeta `tests/` contiene las pruebas de los métodos, la definición de funciones y la generación de archivos CSV y PNG.

## 5. Requisitos

- **Python 3.13** (versión utilizada durante el desarrollo: **3.13.16**).
- Git, para clonar el repositorio y trabajar con ramas.
- Dependencias indicadas en `requirements.txt`: **NumPy**, **Matplotlib** y **Pytest**.

No se necesita Docker: se utiliza un **entorno virtual de Python (`venv`)** para mantener las dependencias aisladas.

## 6. Instalación del entorno

Los comandos siguientes se ejecutan desde una terminal ubicada en la carpeta principal del repositorio.

### Windows (PowerShell)

**1. Clonar el repositorio y entrar a la carpeta:**

```powershell
git clone https://github.com/SadKeflon/evaluacion2-busqueda-raices.git
cd evaluacion2-busqueda-raices
```

**2. Crear y activar el entorno virtual:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell impide activar el entorno, se puede habilitar la ejecución de scripts **solo para la sesión actual**:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

**3. Instalar las dependencias:**

```powershell
python -m pip install -r requirements.txt
```

**4. Comprobar la instalación:**

```powershell
python --version
python -m pytest --version
```

### Linux / macOS

```bash
git clone https://github.com/SadKeflon/evaluacion2-busqueda-raices.git
cd evaluacion2-busqueda-raices
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 7. Ejecución del laboratorio

**Importante:** ejecutar todos los comandos desde la raíz del repositorio, con el entorno virtual activo. El siguiente orden permite reproducir los resultados sin depender de archivos creados manualmente.

### Paso 1. Ejecutar los experimentos y generar los CSV

```powershell
python -m src.scripts.experimentos
```

El programa aplica los seis métodos a las seis funciones, es decir, **36 combinaciones**. Cuando un método no aplica o no converge, se registra esa situación sin considerarla una raíz válida.

En `src/data/` se crean o actualizan:

```text
polinomica.csv
raiz_doble.csv
logaritmica.csv
exponencial.csv
trigonometrica.csv
mixta.csv
resumen_metodos.csv
```

Los seis primeros archivos contienen las columnas `x` y `f(x)`; por defecto se evalúan **201 puntos** por función. El archivo `resumen_metodos.csv` contiene:

```text
funcion,metodo,raiz,iteraciones,error,convergio
```

### Paso 2. Generar los gráficos de las funciones

```powershell
python -m src.scripts.graficos_funciones
```

Se generan seis imágenes PNG en `src/assets/`, una por función. Cada figura muestra la curva, el eje horizontal y la raíz aproximada marcada cuando corresponde.

### Paso 3. Generar los gráficos de convergencia

```powershell
python -m src.scripts.graficos_convergencia
```

Se generan seis imágenes con nombres como `convergencia_polinomica.png` y `convergencia_raiz_doble.png`.

Se representa `log10(error)` frente a la iteración, utilizando los valores positivos del historial de cada método. En general, el error registrado es una medida de cambio entre aproximaciones consecutivas; **no debe confundirse automáticamente con el error verdadero respecto a una raíz exacta**. La convención de la primera iteración depende del método.

### Paso 4. Generar la comparación de iteraciones

```powershell
python -m src.scripts.grafico_iteraciones
```

Este programa lee `src/data/resumen_metodos.csv` y guarda `src/assets/comparacion_iteraciones.png`. En el gráfico, **NC** indica que un método no convergió o no pudo aplicarse; no significa que encontró la raíz en cero iteraciones.

### Ejecutar toda la secuencia

```powershell
python -m src.scripts.experimentos
python -m src.scripts.graficos_funciones
python -m src.scripts.graficos_convergencia
python -m src.scripts.grafico_iteraciones
```

Si Matplotlib presenta errores relacionados con `tkinter` o `Tcl/Tk`, se puede seleccionar el motor de gráficos sin ventanas antes de ejecutar los programas:

```powershell
$env:MPLBACKEND = "Agg"
```

Este ajuste permite crear los PNG sin abrir ventanas gráficas.

## 8. Gráficos y resultados

Las imágenes de `src/assets/` permiten comprobar tres aspectos solicitados en el laboratorio:

1. **Funciones y raíces:** seis gráficos individuales, con la tangencia al eje en el caso de raíz doble.
2. **Convergencia:** seis gráficos que comparan la evolución del error de los métodos sobre cada función.
3. **Resumen:** un gráfico de barras que compara la cantidad de iteraciones por función y método.

Los resultados dependen de los valores iniciales y de las condiciones de parada de cada implementación. **Un método puede no converger o no ser aplicable en un caso particular**, y eso forma parte del análisis.

En particular, para las raíces múltiples, un valor pequeño de `|f(x)|` no siempre garantiza la misma precisión en `x` que en una raíz simple; por ello conviene examinar tanto las aproximaciones como los criterios de parada.

## 9. Pruebas automáticas

Las pruebas están escritas con **Pytest**. Para ejecutarlas todas:

```powershell
python -m pytest -v
```

También se pueden ejecutar pruebas individuales, por ejemplo:

```powershell
python -m pytest tests/test_biseccion.py -v
python -m pytest tests/test_newton_mejorado.py -v
python -m pytest tests/test_experimentos.py -v
```

Las pruebas comprueban resultados numéricos, situaciones donde un método no puede avanzar y la generación de archivos de salida. Se recomienda ejecutarlas antes de cada commit y antes de fusionar un Pull Request.

**GitHub Actions:** si se incluye el archivo `.github/workflows/pruebas.yml`, GitHub podrá ejecutar las pruebas automáticamente al recibir cambios y Pull Requests, según los eventos configurados. Su existencia y el estado de las ejecuciones deben comprobarse en la pestaña **Actions** del repositorio; las pruebas locales no garantizan por sí solas que el flujo remoto esté aprobado.

## 10. Trabajo colaborativo con Git y GitHub

El proyecto se desarrolla en un repositorio compartido, con una rama principal y una rama por integrante:

| Rama | Uso |
|---|---|
| `main` | Código integrado y considerado para la evaluación. |
| `kevin-villarroel` | Desarrollo de Kevin Villarroel. |
| `rodrigo-retamal` | Desarrollo de Rodrigo Retamal. |

El trabajo se distribuyó por funcionalidades: Kevin desarrolló los métodos de bisección, falsa posición y secante, además de componentes de experimentación y convergencia; Rodrigo trabajó en punto fijo, las versiones de Newton y componentes de exportación y gráficos. Los aportes específicos pueden revisarse en el historial de commits y los Pull Requests.

El flujo de colaboración es:

1. Trabajar en la rama propia y ejecutar las pruebas.
2. Crear commits con mensajes que describan el cambio.
3. Publicar la rama en GitHub.
4. Abrir un Pull Request hacia `main` y revisar el código.
5. Integrar solamente cuando los cambios estén comprobados.
6. Actualizar ambas ramas desde `main` para continuar el desarrollo.

**El enunciado indica que solo se evalúa el contenido integrado en `main`.** Por lo tanto, antes de entregar se debe comprobar que los scripts, CSV, PNG, pruebas y documentación estén presentes en esa rama.

## 11. Informe de convergencia

El archivo **`informe.md`** debe complementar este README y responder, utilizando los resultados y gráficos generados:

1. Qué método convergió en menos iteraciones para cada función y por qué.
2. Qué orden de convergencia presenta cada método y cómo se observa en los gráficos.
3. Qué métodos requieren un intervalo con cambio de signo y cuáles no.
4. Qué ocurre en la raíz doble, cuáles métodos no aplican o fallan y cuál se comporta mejor.
5. Cómo afectan los intervalos y las estimaciones iniciales a la convergencia y a las iteraciones.
6. Qué método se recomienda para cada tipo de función considerando velocidad y robustez.

Debe cerrar con una **conclusión argumentada basada en las cifras y gráficos del proyecto**. El README documenta cómo reproducir el trabajo, mientras que `informe.md` presenta el análisis de los resultados.

## 12. Comprobación antes de entregar

- [ ] Los seis métodos están implementados y probados.
- [ ] Las seis funciones y sus condiciones iniciales están definidas.
- [ ] Los siete archivos CSV están generados y revisados.
- [ ] Los seis gráficos de funciones muestran sus raíces; la raíz doble muestra tangencia.
- [ ] Los seis gráficos de convergencia tienen títulos, ejes y leyendas legibles.
- [ ] El gráfico comparativo de iteraciones distingue los casos sin convergencia.
- [ ] `python -m pytest -v` termina sin fallos.
- [ ] `informe.md` contiene las seis respuestas y una conclusión respaldada por datos.
- [ ] `requirements.txt` contiene las dependencias necesarias.
- [ ] Los aportes de ambos integrantes aparecen en el historial Git.
- [ ] Todos los archivos finales están integrados y revisados en `main`.

---

**Universidad Católica del Maule — Computación Numérica — Laboratorio evaluado 2.**
