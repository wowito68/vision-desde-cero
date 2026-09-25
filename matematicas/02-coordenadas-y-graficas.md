---
title: "02 · Coordenadas y gráficas"
layout: default
nav_order: 2
permalink: /matematicas/coordenadas-y-graficas/
parent: "01 · Matemáticas"
---
# 02 · Coordenadas y gráficas

**Duración sugerida:** 60–75 minutos.  
**Requisitos previos:** clase 01; contar posiciones desde cero.  
**Herramientas:** papel cuadriculado; Python es opcional.

## Qué aprenderás

- Ubicar puntos mediante dos coordenadas y distinguir el orden de un par.
- Traducir entre (x, y) en una gráfica y (fila, columna) en una imagen.
- Leer las dimensiones de una imagen y comprobar si una posición es válida.
- Interpretar una gráfica de intensidades sin confundir ubicación con valor.

## 1. Una coordenada localiza un punto

En una recta basta un número para señalar una posición. En un plano hacen falta dos. Un par ordenado (x, y) indica primero la posición horizontal y después la vertical. **El orden importa:** (2, 1) y (1, 2) son puntos distintos.

En el plano cartesiano habitual, x aumenta hacia la derecha e y hacia arriba. Una imagen digital suele dibujarse con el origen en la esquina superior izquierda: la **columna** aumenta hacia la derecha y la **fila** hacia abajo.

| Contexto | Primera coordenada | Segunda coordenada | Origen habitual |
|---|---|---|---|
| Gráfica cartesiana (x, y) | horizontal | vertical hacia arriba | intersección de los ejes |
| Imagen (fila, columna) | vertical hacia abajo | horizontal | esquina superior izquierda |

Para pasar de (fila, columna) a una convención gráfica con el mismo origen y eje vertical hacia abajo, usamos x = columna, y = fila. Si la gráfica usa origen inferior izquierdo y eje vertical hacia arriba, para una imagen de altura H indexada desde cero usamos x = columna, y = H - 1 - fila.

## 2. Una imagen diminuta

Considera esta imagen de **3 filas y 4 columnas** en escala de grises:

~~~text
         columna 0   1   2   3
fila 0           0  40  80 120
fila 1          20  60 100 140
fila 2          30  70 110 150
~~~

La intensidad en (fila=1, columna=2) es **100**. La posición es el par (1, 2); el valor almacenado allí es 100. No debemos confundir coordenadas con intensidad.

Si escribimos I(f, c) para la intensidad de la fila f y la columna c, entonces I(1, 2) = 100. Esta notación describe una función de **dos entradas**. Su dominio son los pares válidos: f entre 0 y 2, c entre 0 y 3.

### Comprobación de límites

Para una imagen de altura H y anchura W, una posición (f, c) es válida si 0 ≤ f < H y 0 ≤ c < W. En el ejemplo, (2, 3) es válido y vale 150; (3, 2) no lo es. El índice máximo de fila es H - 1, no H.

## 3. Una gráfica de una fila

Tomemos la fila 1: [20, 60, 100, 140]. Podemos graficar los pares (columna, intensidad):

~~~text
(0, 20), (1, 60), (2, 100), (3, 140)
~~~

Esta gráfica tiene una sola coordenada espacial en el eje horizontal. El eje vertical muestra el **valor** del píxel, no su fila. La fila ya quedó fijada en 1. El aumento constante de 40 unidades entre columnas produce una recta en la gráfica; no significa que los píxeles formen una diagonal dentro de la imagen.

## 4. Primer acceso con Python

Una lista de listas puede representar filas de una imagen sin instalar bibliotecas:

~~~python
imagen = [
    [0, 40, 80, 120],
    [20, 60, 100, 140],
    [30, 70, 110, 150],
]

alto = len(imagen)
ancho = len(imagen[0])
fila, columna = 1, 2
print(alto, ancho)                 # 3 4
print(imagen[fila][columna])       # 100
print(list(enumerate(imagen[1]))) # [(0, 20), (1, 60), (2, 100), (3, 140)]
~~~

Aquí suponemos que todas las filas tienen el mismo largo y que la imagen no está vacía. En una biblioteca de imágenes, esos supuestos se comprueban o vienen garantizados por el tipo de dato.

## 5. Ejercicios

1. ¿Qué valor tiene I(2, 1)? ¿Y I(0, 3)?
2. Señala cuáles posiciones son válidas: (0, 0), (2, 3), (3, 0), (1, 4).
3. Para la fila 0, escribe los cuatro pares (columna, intensidad) de su gráfica.
4. Una imagen mide 480 píxeles de alto y 640 de ancho. ¿Cuál es su última posición válida? ¿Es válida (480, 100)?
5. En una imagen de altura 3, convierte (fila=0, columna=2) a coordenadas cartesianas con origen inferior izquierdo.

## 6. Respuestas razonadas

1. I(2, 1) = 70 e I(0, 3) = 120.
2. Las dos primeras son válidas. La fila 3 y la columna 4 exceden los límites.
3. (0, 0), (1, 40), (2, 80), (3, 120); el primer número de cada par es la columna, el segundo la intensidad.
4. (479, 639); (480, 100) no es válida porque las filas van de 0 a 479.
5. x = 2, y = 3 - 1 - 0 = 2; el punto es (2, 2).

## 7. Conexión con visión por computadora

Una detección puede señalar una caja mediante coordenadas, un filtro puede leer los vecinos de un píxel y una red puede producir un mapa de características. Todas esas operaciones dependen de saber qué representa cada eje y dónde empiezan los índices. En el siguiente tema, un píxel de color será un **vector** de tres componentes.

## Recursos para profundizar

**Gratuitos**

- [Khan Academy: plano coordenado](https://es.khanacademy.org/math/geometry-home/geometry-coordinate-plane) — vídeos y práctica interactiva para ubicar pares ordenados; empieza por «Plano coordenado: cuadrante 1».
- [NumPy: indexación de arreglos](https://numpy.org/doc/stable/user/basics.indexing.html) — referencia oficial sobre índices desde cero y acceso por fila y columna (inglés).
- [MIT: *Foundations of Computer Vision*, representación de imágenes y geometría](https://visionbook.mit.edu/homogeneous_coordinates.html) — lectura abierta más avanzada; basta la introducción por ahora.

**Libro comercial opcional**

- [Gonzalez y Woods, *Digital Image Processing*, 4.ª ed.](https://www.pearson.com/en-us/subject-catalog/p/Gonzalez-Digital-Image-Processing-4th-Edition/P200000003224/9780133356724) — consulta sobre imágenes digitales y geometría. Este curso ofrece los conceptos necesarios sin comprarlo.
