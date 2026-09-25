---
title: "03 · Vectores y color RGB"
layout: default
nav_order: 3
permalink: /matematicas/vectores-y-color-rgb/
parent: "01 · Matemáticas"
---
# 03 · Vectores y color RGB
**Duración sugerida:** 75–90 minutos.
**Requisitos previos:** clases 01 y 02; sumas y cuadrados.
**Herramientas:** papel, calculadora sencilla; Python es opcional.
## Qué aprenderás
- Interpretar un vector como una lista ordenada de componentes.
- Sumar vectores, multiplicarlos por un escalar y calcular una distancia.
- Representar un píxel RGB como un vector de tres componentes.
- Distinguir distancia numérica entre colores de semejanza perceptual.
## 1. De un número a tres componentes
Un píxel en escala de grises puede expresarse con una intensidad, como 100. Un píxel RGB se representa mediante tres cantidades ordenadas: **rojo, verde y azul**. En RGB de 8 bits por canal, (255, 0, 0) representa rojo puro y (0, 0, 0) negro. Cada componente está entre 0 y 255.
Un **vector** es una colección ordenada de números. Por ejemplo, p = (120, 80, 40) es un vector de tres componentes. Que sean valores RGB es una interpretación concreta; matemáticamente también podríamos usar el mismo vector para describir tres mediciones distintas.
El orden importa: (255, 0, 0) y (0, 0, 255) tienen los mismos números, pero representan colores diferentes. Algunas bibliotecas trabajan con BGR en vez de RGB; siempre hay que revisar la convención de la herramienta.
## 2. Suma y multiplicación por un escalar
Las operaciones se realizan componente a componente:
```plain text
(10, 20, 30) + (2, 3, 4) = (12, 23, 34)
2 · (10, 20, 30) = (20, 40, 60)
```
Como ejemplo de iluminación, sumemos (30, 30, 30) al color (120, 80, 40). Obtendremos (150, 110, 70). Si un canal supera 255, debemos decidir cómo manejarlo; para una salida RGB de 8 bits podemos recortarlo a 255, igual que en la clase 01.
La multiplicación por 0.5 produce (60, 40, 20) en este caso. Para vectores generales, el resultado puede incluir decimales; una imagen de 8 bits necesita una regla adicional de redondeo y conversión. No confundamos la operación matemática con la codificación final.
## 3. Magnitud y distancia
La **magnitud euclidiana** de un vector v = (a, b, c) es \|\|v\|\| = √(a² + b² + c²). Por ejemplo, \|\|(3, 4, 0)\|\| = 5. Esta fórmula generaliza el teorema de Pitágoras.
La distancia entre dos vectores es la magnitud de su diferencia:
```plain text
d(p, q) = ||p - q||
```
Para p = (10, 20, 30) y q = (13, 24, 30), la diferencia es (-3, -4, 0) y la distancia es √(9 + 16) = 5. Para decidir cuál de varios colores RGB es numéricamente más cercano a una referencia, podemos comparar estas distancias.
**Límite importante:** la distancia euclidiana en RGB no equivale necesariamente a la diferencia que percibe una persona. Depende también del espacio de color, la iluminación y la visualización. Más adelante estudiaremos espacios como CIELAB y cuándo conviene utilizarlos.
## 4. Ejemplo en Python sin dependencias
```python
from math import dist

p = (120, 80, 40)
incremento = (30, 30, 30)

def sumar_color(a, b):
    return tuple(min(x + y, 255) for x, y in zip(a, b))

print(sumar_color(p, incremento))  # (150, 110, 70)
print(dist((10, 20, 30), (13, 24, 30)))  # 5.0
```
zip empareja las componentes que ocupan la misma posición. Este ejemplo supone que ambos colores tienen exactamente tres componentes y que las entradas ya son enteros RGB válidos. En producción comprobaríamos esos supuestos explícitamente.
## 5. Ejercicios
1. Suma (20, 40, 60) y (5, 10, 15).
2. Calcula 3 · (2, 4, 6).
3. Aplica un incremento RGB de (20, 20, 20) a (250, 100, 0) con recorte a 255.
4. Calcula la distancia entre (0, 0, 0) y (0, 3, 4).
5. Considera la referencia (100, 100, 100). ¿Cuál de (101, 100, 100) y (110, 100, 100) está más cerca?
6. Explica por qué una distancia RGB pequeña no garantiza que dos colores se vean igualmente parecidos en todas las condiciones.
## 6. Respuestas razonadas
1. (25, 50, 75).
2. (6, 12, 18).
3. La suma da (270, 120, 20); al recortar queda (255, 120, 20).
4. √(0² + 3² + 4²) = 5.
5. El primero: las distancias son 1 y 10, respectivamente.
6. RGB es una codificación de canales, no una medida uniforme de percepción; pantalla, iluminación y espacio de color influyen en lo que vemos.
## 7. Conexión con visión por computadora
Una imagen RGB se puede pensar como una cuadrícula en la que cada posición contiene un vector de tres números. Algunos algoritmos comparan vectores para agrupar colores, seguir objetos o calcular diferencias. En la próxima clase colocaremos esos vectores en una estructura de **filas y columnas**: las matrices.
## Recursos para profundizar
**Gratuitos**
- [OpenStax: vectores](https://openstax.org/books/precalculus/pages/8-8-vectors) — libro abierto con operaciones y magnitud (inglés).
- [Pillow: bandas y modos RGB](https://pillow.readthedocs.io/en/stable/handbook/concepts.html) — documentación oficial de canales y profundidad de bits (inglés).
- [MIT: ](https://visionbook.mit.edu/)[*Foundations of Computer Vision*](https://visionbook.mit.edu/) — libro en línea gratuito para conectar color, imágenes y geometría; sus capítulos posteriores son avanzados.
**Libro comercial opcional**
- [Lay, Lay y McDonald, ](https://www.pearson.com/en-us/subject-catalog/p/linear-algebra-and-its-applications/P200000006235)[*Linear Algebra and Its Applications*](https://www.pearson.com/en-us/subject-catalog/p/linear-algebra-and-its-applications/P200000006235)[, 6.ª ed.](https://www.pearson.com/en-us/subject-catalog/p/linear-algebra-and-its-applications/P200000006235) — desarrollo extenso de vectores y álgebra lineal. Los ejercicios de esta clase no dependen del libro.
