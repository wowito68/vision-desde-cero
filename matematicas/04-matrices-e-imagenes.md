---
title: "04 · Matrices e imágenes"
layout: default
nav_order: 4
permalink: /matematicas/matrices-e-imagenes/
parent: "01 · Matemáticas"
---
# 04 · Matrices e imágenes

**Duración sugerida:** 75–90 minutos.  
**Requisitos previos:** clases 01–03; filas, columnas y vectores.  
**Herramientas:** papel; Python y NumPy opcionales.

## Qué aprenderás

- Reconocer una matriz y describir su tamaño como filas × columnas.
- Representar una imagen en escala de grises como matriz.
- Sumar matrices del mismo tamaño y multiplicarlas por un escalar.
- Entender por qué una imagen RGB suele requerir tres dimensiones de datos.
- Distinguir operaciones por elemento del producto matricial.

## 1. De la cuadrícula a la matriz

Una **matriz** es un arreglo rectangular de números. Esta matriz A tiene 2 filas y 3 columnas, así que su tamaño es 2 × 3:

~~~text
A = [  0   40   80
      20   60  100 ]
~~~

La entrada de la fila 1 y columna 2 es 100 si empezamos a contar desde cero, como en Python. En matemáticas es frecuente escribir índices desde uno; por eso conviene declarar la convención antes de usar símbolos como Aᵢⱼ.

Una imagen en escala de grises puede guardarse como una matriz de intensidades. El **tamaño** indica cuántas posiciones hay, no el valor máximo de sus píxeles. A contiene 2 × 3 = 6 intensidades.

## 2. Operaciones por elemento

Dos matrices del mismo tamaño se suman posición por posición. Si B también mide 2 × 3:

~~~text
B = [ 10  10  10
      10  10  10 ]

A + B = [ 10  50   90
          30  70  110 ]
~~~

Para aumentar el brillo de la imagen sumamos una constante a cada entrada y después aplicamos recorte si la representación lo exige. Multiplicar A por 2 duplica cada entrada, pero no duplica sus dimensiones.

Estas son **operaciones por elemento**. El **producto matricial** es una operación diferente, definida solo cuando coinciden las dimensiones internas. Lo estudiaremos en la siguiente clase; escribir A * B en una biblioteca no siempre significa producto matricial.

## 3. Imagen RGB: alto × ancho × canales

Si cada píxel guarda un vector RGB, ya no basta una matriz de números escalares. Una representación habitual tiene forma alto × ancho × 3. Por ejemplo, una imagen de 2 × 3 píxeles RGB puede verse como tres matrices de 2 × 3, una por canal rojo, otra por verde y otra por azul, o como una cuadrícula de seis vectores RGB.

Una **matriz** tiene dos ejes; el arreglo RGB descrito tiene tres y suele llamarse **tensor** en este contexto. Hay otras convenciones, como canales × alto × ancho, especialmente en modelos de aprendizaje profundo. Nunca debemos asumir el orden sin mirar la documentación o la forma real del arreglo.

## 4. Ejemplo con Python puro

~~~python
imagen = [
    [0, 40, 80],
    [20, 60, 100],
]

def aumentar_brillo(matriz, incremento):
    return [
        [min(valor + incremento, 255) for valor in fila]
        for fila in matriz
    ]

resultado = aumentar_brillo(imagen, 30)
print(resultado)  # [[30, 70, 110], [50, 90, 130]]
print(len(resultado), len(resultado[0]))  # 2 3
~~~

La función crea una nueva lista de listas; no cambia imagen. Se supone que la entrada es rectangular y contiene intensidades de 8 bits. Cuando usemos NumPy, revisaremos además el tipo de dato para evitar desbordamientos al sumar.

## 5. Ejercicios

1. ¿Cuántas entradas tiene una matriz de 4 × 5? ¿Cuál es el índice de su última fila en Python?
2. Suma [[1, 2], [3, 4]] y [[10, 20], [30, 40]] por elemento.
3. Multiplica [[2, 4], [6, 8]] por el escalar 0.5.
4. ¿Se pueden sumar por elemento una matriz 2 × 3 y otra 3 × 2 siguiendo la regla dada aquí?
5. ¿Qué forma tendría un arreglo alto × ancho × canales para una imagen RGB de 480 filas y 640 columnas?
6. Si sumas 30 a una matriz de uint8 con una entrada 240, ¿qué precaución debes tomar antes de guardar el resultado?

## 6. Respuestas razonadas

1. 20 entradas; las filas se indexan 0, 1, 2, 3, así que el último índice es 3.
2. [[11, 22], [33, 44]].
3. [[1, 2], [3, 4]].
4. No: las dimensiones deben coincidir para esta suma.
5. (480, 640, 3) en esa convención. Una biblioteca que use canales primero tendría (3, 480, 640).
6. Calcular en un tipo suficientemente amplio y recortar a 255 antes de convertir de nuevo a uint8; la suma directa puede desbordarse.

## 7. Conexión con visión por computadora

Filtros, máscaras, mapas de profundidad y activaciones de redes pueden representarse como arreglos numéricos. Conocer sus dimensiones evita mezclar un canal con una coordenada o aplicar una operación a ejes equivocados. La próxima clase explicará cómo el producto matricial describe transformaciones y combinaciones lineales.

## Recursos para profundizar

**Gratuitos**

- [OpenStax: matrices y operaciones](https://openstax.org/books/precalculus/pages/9-5-matrices-and-matrix-operations) — capítulo abierto con suma, escalares y producto (inglés).
- [NumPy: introducción a arreglos multidimensionales](https://numpy.org/doc/stable/user/quickstart.html) — ejemplos oficiales de shape, indexación y operaciones (inglés).
- [Pillow: conceptos de imagen y canales](https://pillow.readthedocs.io/en/stable/handbook/concepts.html) — referencia oficial para relacionar filas, columnas y bandas (inglés).

**Libros comerciales opcionales**

- [Lay, Lay y McDonald, *Linear Algebra and Its Applications*, 6.ª ed.](https://www.pearson.com/en-us/subject-catalog/p/linear-algebra-and-its-applications/P200000006235) — desarrollo detallado de matrices y transformaciones.
- [Gonzalez y Woods, *Digital Image Processing*, 4.ª ed.](https://www.pearson.com/en-us/subject-catalog/p/Gonzalez-Digital-Image-Processing-4th-Edition/P200000003224/9780133356724) — aplicación a imágenes digitales. Ambos son complementarios.
