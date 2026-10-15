# Informe de convergencia - Evaluacion 2: Busqueda de raices

## 1. Objetivo y ambiente de pruebas

El objetivo de este laboratorio fue comparar seis metodos numericos para la busqueda de raices:

- Biseccion
- Falsa posicion
- Punto fijo
- Secante
- Newton-Raphson
- Newton-Raphson mejorado

Para realizar la comparacion se utilizaron seis funciones de distintos tipos, incluyendo una funcion con raiz doble.

En todos los experimentos se utilizaron las mismas condiciones generales:

- Tolerancia: 1e-6
- Maximo de iteraciones: 100
- Intervalos definidos para cada funcion
- Valores iniciales definidos para los metodos abiertos

Los resultados de cada metodo registran:

- Raiz aproximada
- Numero de iteraciones
- Error
- Estado de convergencia
- Historial de iteraciones

## 2. Funciones utilizadas

Las funciones utilizadas durante el laboratorio fueron las siguientes:

| Funcion | Expresion | Intervalo | Valores iniciales |
|---|---|---|---|
| Polinomica | x^3 - x - 2 | [1, 2] | p0 = 1.5, p1 = 2.0 |
| Raiz doble | (x - 2)^2 | [1, 3] | p0 = 1.2, p1 = 2.5 |
| Logaritmica | ln(x) + x - 4 | [2, 3] | p0 = 2.5, p1 = 3.0 |
| Exponencial | exp(-x) - x | [0, 1] | p0 = 0.5, p1 = 1.0 |
| Trigonometrica | cos(x) - x | [0, 1] | p0 = 0.5, p1 = 1.0 |
| Mixta | sqrt(x) - cos(x) | [0.1, 1] | p0 = 0.5, p1 = 1.0 |

## 3. Comprobacion de las raices en los intervalos

Para los metodos cerrados es necesario revisar si existe un cambio de signo entre los extremos del intervalo.

Los resultados obtenidos fueron:

| Funcion | f(a) | f(b) | Cambio de signo |
|---|---:|---:|---|
| Polinomica | -2.000000 | 4.000000 | Si |
| Logaritmica | -1.306853 | 0.098612 | Si |
| Exponencial | 1.000000 | -0.632121 | Si |
| Trigonometrica | 1.000000 | -0.459698 | Si |
| Mixta | -0.678776 | 0.459698 | Si |

En estos casos se cumple:

f(a) * f(b) < 0

Por lo tanto, al ser funciones continuas dentro de los intervalos utilizados, existe al menos una raiz dentro de ellos.

El caso de la raiz doble es diferente.

La funcion es:

f(x) = (x - 2)^2

Se obtiene:

f(1) = 1

f(2) = 0

f(3) = 1

La funcion llega a cero en x = 2, pero no cambia de signo. Esto significa que la curva toca el eje horizontal sin cruzarlo.

Por esta razon, los metodos de biseccion y falsa posicion no pueden utilizarse normalmente con el intervalo [1, 3].

## 4. Resultados generales

El archivo resumen_metodos.csv contiene 36 ejecuciones, correspondientes a los seis metodos aplicados a las seis funciones.

De las 36 ejecuciones:

- 33 registraron convergencia.
- 3 no convergieron o no pudieron aplicarse.

La cantidad de iteraciones obtenida fue la siguiente:

| Funcion | Biseccion | Falsa posicion | Punto fijo | Secante | Newton | Newton mejorado |
|---|---:|---:|---:|---:|---:|---:|
| Polinomica | 22 | 13 | 7 | 4 | 2 | 2 |
| Raiz doble | NC | NC | NC (100) | 15 | 10 | 1 |
| Logaritmica | 19 | 4 | 14 | 3 | 3 | 3 |
| Exponencial | 20 | 7 | 22 | 3 | 2 | 2 |
| Trigonometrica | 20 | 5 | 34 | 4 | 3 | 3 |
| Mixta | 20 | 4 | 5 | 3 | 2 | 2 |

NC significa que el metodo no convergio o no pudo aplicarse.

Algunas de las raices aproximadas obtenidas con Newton-Raphson mejorado fueron:

| Funcion | Raiz aproximada |
|---|---:|
| Polinomica | 1.521380 |
| Raiz doble | 2.000000 |
| Logaritmica | 2.926271 |
| Exponencial | 0.567143 |
| Trigonometrica | 0.739085 |
| Mixta | 0.641714 |

## 5. Analisis de convergencia

### 5.1. Que metodo convergio en menos iteraciones para cada funcion?

Para la funcion polinomica, Newton-Raphson y Newton mejorado necesitaron solamente 2 iteraciones.

Para la raiz doble, Newton mejorado fue claramente el metodo mas rapido, utilizando solamente 1 iteracion.

Para la funcion logaritmica, secante, Newton-Raphson y Newton mejorado necesitaron 3 iteraciones.

Para la funcion exponencial, Newton-Raphson y Newton mejorado utilizaron 2 iteraciones.

Para la funcion trigonometrica, Newton-Raphson y Newton mejorado necesitaron 3 iteraciones.

Para la funcion mixta, Newton-Raphson y Newton mejorado utilizaron 2 iteraciones.

En general, Newton-Raphson fue uno de los metodos mas rapidos debido a que utiliza informacion de la derivada para mejorar cada aproximacion.

La secante tambien entrego buenos resultados sin necesitar calcular derivadas.

Biseccion fue mas lento que los metodos abiertos, pero mantuvo un comportamiento estable en todos los casos donde existia cambio de signo.

### 5.2. Orden de convergencia de los metodos

Los metodos estudiados presentan distintos comportamientos de convergencia.

Biseccion presenta convergencia lineal. En cada iteracion reduce aproximadamente a la mitad el intervalo donde se encuentra la raiz.

Falsa posicion generalmente presenta convergencia lineal. Dependiendo de la forma de la funcion, uno de los extremos puede mantenerse casi fijo durante varias iteraciones.

Punto fijo depende directamente de la funcion g(x) utilizada. Para que exista convergencia cerca de la raiz, se busca que el valor absoluto de la derivada de g sea menor que 1.

Secante presenta convergencia superlineal y normalmente es mas rapido que los metodos cerrados.

Newton-Raphson presenta convergencia cuadratica cerca de una raiz simple cuando se cumplen las condiciones necesarias.

Newton-Raphson mejorado utiliza la primera y segunda derivada, y permite mejorar el comportamiento en problemas con raices multiples.

Los graficos generados muestran log10(error) respecto del numero de iteraciones.

Cuando la curva disminuye rapidamente significa que el error entre aproximaciones tambien disminuye rapidamente.

Los metodos Newton y secante presentan normalmente una disminucion mas rapida del error que biseccion.

### 5.3. Que metodos necesitan cambio de signo?

Los metodos que necesitan un intervalo con cambio de signo son:

- Biseccion
- Falsa posicion

Para estos metodos se necesita que:

f(a) * f(b) < 0

Los metodos abiertos no necesitan esta condicion:

- Punto fijo
- Secante
- Newton-Raphson
- Newton-Raphson mejorado

Sin embargo, estos metodos dependen mas de los valores iniciales y de las propiedades de la funcion.

Por esta razon pueden converger rapidamente, pero tambien pueden divergir o detenerse si las condiciones no son adecuadas.

### 5.4. Que ocurrio con la raiz doble?

La funcion utilizada fue:

f(x) = (x - 2)^2

La raiz exacta es:

x = 2

En esta funcion no existe cambio de signo alrededor de la raiz.

Por este motivo, biseccion y falsa posicion no pudieron aplicarse con el intervalo [1, 3].

Punto fijo tampoco logro cumplir el criterio de convergencia despues de 100 iteraciones.

Los otros metodos obtuvieron los siguientes resultados:

| Metodo | Iteraciones | Raiz obtenida | Error respecto de x = 2 |
|---|---:|---:|---:|
| Secante | 15 | 2.000825423 | 0.000825423 |
| Newton-Raphson | 10 | 1.999218750 | 0.000781250 |
| Newton mejorado | 1 | 2.000000000 | 0.000000000 |

El mejor comportamiento correspondio a Newton-Raphson mejorado.

Este metodo encontro x = 2 en una sola iteracion desde el valor inicial utilizado.

La formula implementada fue:

p = p0 - (f(p0) * f'(p0)) / ((f'(p0))^2 - f(p0) * f''(p0))

Tambien se observo que secante y Newton-Raphson normal fueron registrados como convergentes aunque sus aproximaciones todavia estaban a aproximadamente 0.0008 de la raiz exacta.

Esto ocurre porque para una raiz doble un valor pequeño de abs(f(x)) no significa necesariamente que el valor de x este igualmente cerca de la raiz.

Por ejemplo:

f(x) = (x - 2)^2

Si:

abs(f(x)) < 1e-6

entonces aproximadamente:

abs(x - 2) < 0.001

Por esta razon es importante distinguir entre:

- Residuo: abs(f(x))
- Diferencia entre aproximaciones: abs(x_n - x_anterior)
- Error verdadero respecto de la raiz exacta

### 5.5. Como influyen el intervalo y los valores iniciales?

Para estudiar esta situacion se realizaron nueve pruebas adicionales utilizando la funcion:

f(x) = x^3 - x - 2

Se mantuvieron constantes:

- Tolerancia = 1e-6
- Maximo de iteraciones = 100

Solamente se modificaron los intervalos o los valores iniciales.

Los resultados obtenidos fueron:

| Metodo | Condiciones | Iteraciones | Raiz | Residuo |
|---|---|---:|---:|---:|
| Biseccion | [1, 2] | 22 | 1.521379709 | 1.4498e-08 |
| Biseccion | [1.4, 1.6] | 18 | 1.521379852 | 8.6476e-07 |
| Biseccion | [1.5, 1.55] | 16 | 1.521379852 | 8.6476e-07 |
| Newton-Raphson | p0 = 1 | 5 | 1.521379710 | 1.7407e-08 |
| Newton-Raphson | p0 = 1.5 | 2 | 1.521379806 | 5.8939e-07 |
| Newton-Raphson | p0 = 2 | 4 | 1.521379710 | 1.7407e-08 |
| Secante | p0 = 1, p1 = 2 | 6 | 1.521379708 | 7.0155e-09 |
| Secante | p0 = 1.4, p1 = 1.6 | 4 | 1.521379706 | 4.9929e-09 |
| Secante | p0 = 1.5, p1 = 1.6 | 3 | 1.521379776 | 4.1377e-07 |

Los nueve casos convergieron correctamente y presentaron un residuo menor que 1e-6.

En biseccion se observo que al disminuir el tamaño del intervalo tambien disminuyo la cantidad de iteraciones.

Con el intervalo [1, 2] fueron necesarias 22 iteraciones.

Con [1.4, 1.6] fueron necesarias 18.

Con [1.5, 1.55] fueron necesarias 16.

Esto ocurre porque un intervalo inicial mas pequeño necesita menos subdivisiones para acercarse a la raiz.

En Newton-Raphson tambien existieron diferencias dependiendo del valor inicial.

Con p0 = 1 fueron necesarias 5 iteraciones.

Con p0 = 1.5 fueron necesarias solamente 2.

Con p0 = 2 fueron necesarias 4.

Para esta funcion, el valor inicial p0 = 1.5 fue el mas favorable de los tres valores estudiados.

En secante ocurrio algo parecido.

Con los valores 1 y 2 fueron necesarias 6 iteraciones.

Con 1.4 y 1.6 fueron necesarias 4.

Con 1.5 y 1.6 solamente fueron necesarias 3.

Los resultados muestran que las condiciones iniciales pueden afectar de manera importante la cantidad de iteraciones necesarias.

Sin embargo, esto no significa que elegir siempre el intervalo mas pequeño o el valor mas cercano a la raiz garantice mejores resultados para cualquier funcion.

Tambien se debe considerar que un metodo que utiliza menos iteraciones no necesariamente termina con un residuo menor.

Por ejemplo, Newton desde p0 = 1.5 necesito solamente 2 iteraciones y termino con un residuo cercano a 5.89e-07.

Desde p0 = 1 necesito 5 iteraciones, pero termino con un residuo cercano a 1.74e-08.

### 5.6. Que metodo recomendamos?

Si existe una derivada disponible y se tiene una aproximacion inicial adecuada, Newton-Raphson es una buena alternativa debido a su velocidad.

En las funciones polinomica, exponencial y mixta necesito solamente 2 iteraciones.

En la funcion trigonometrica necesito 3 iteraciones.

Cuando no se quiere calcular una derivada, secante puede ser una buena opcion.

En las funciones con raiz simple necesito aproximadamente entre 3 y 4 iteraciones en varias de las pruebas realizadas.

Cuando se conoce un intervalo con cambio de signo y se busca un metodo sencillo y estable, biseccion es una opcion confiable, aunque normalmente necesita mas iteraciones.

Falsa posicion puede mejorar la velocidad respecto de biseccion. Por ejemplo, en la funcion logaritmica falsa posicion utilizo 4 iteraciones, mientras biseccion necesito 19.

Para una raiz doble, el metodo que presento mejores resultados fue Newton-Raphson mejorado.

En nuestro experimento encontro exactamente x = 2 en una sola iteracion.

Punto fijo depende fuertemente de la eleccion de g(x). En la funcion mixta convergio en 5 iteraciones, mientras que en la raiz doble no logro converger dentro de las 100 iteraciones permitidas.

## 6. Conclusion

Los experimentos muestran que no existe un metodo que sea siempre el mejor para todos los problemas.

En las funciones con raices simples, Newton-Raphson y Newton-Raphson mejorado fueron generalmente los metodos que necesitaron menos iteraciones.

Secante tambien presento buenos resultados, con la ventaja de que no necesita calcular derivadas.

Biseccion necesito mas iteraciones, pero fue estable en los casos donde existia un intervalo con cambio de signo.

El caso de la raiz doble permitio observar una diferencia importante.

Aunque f(x) = (x - 2)^2 tiene una raiz en x = 2, la funcion no cambia de signo alrededor de ella.

Por esto, los metodos cerrados de biseccion y falsa posicion no pudieron utilizarse con el intervalo elegido.

Newton-Raphson mejorado fue el metodo que presento el mejor comportamiento en este caso, encontrando la raiz en una sola iteracion.

Tambien se comprobo que las condiciones iniciales influyen en la cantidad de iteraciones.

Para la funcion polinomica, biseccion disminuyo desde 22 hasta 16 iteraciones cuando se redujo el intervalo inicial.

Newton-Raphson utilizo entre 2 y 5 iteraciones dependiendo de p0.

Secante utilizo entre 3 y 6 iteraciones dependiendo de sus dos valores iniciales.

Por lo tanto, al seleccionar un metodo numerico no solo se debe considerar su velocidad.

Tambien es necesario considerar:

- El tipo de funcion
- La existencia de derivadas
- La disponibilidad de un intervalo con cambio de signo
- Los valores iniciales
- La precision requerida
- La posibilidad de tener raices multiples

Los resultados obtenidos permiten concluir que los metodos abiertos pueden ser mas rapidos, mientras que los metodos cerrados ofrecen mayor seguridad cuando se cumplen sus condiciones de aplicacion.

## 7. Archivos relacionados

Los principales archivos utilizados para realizar este analisis son:

- src/data/resumen_metodos.csv
- src/data/comparacion_condiciones.csv
- src/data/ con los valores de cada funcion
- src/assets/ con los graficos generados
- src/scripts/ con los metodos numericos y programas de experimentacion

Los resultados presentados en este informe corresponden a las ejecuciones realizadas durante el laboratorio.