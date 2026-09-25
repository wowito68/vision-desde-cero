# 01 · Números, variables y funciones
**Duración sugerida:** 45–60 minutos.
**Requisitos previos:** sumar, restar y comparar números.
**Herramientas:** lápiz y papel; Python es opcional.
## Qué aprenderás
Al terminar esta clase podrás:
- Distinguir un número concreto de una variable.
- Leer una función como una regla que transforma entradas en salidas.
- Calcular una función sencilla y describir su dominio y su rango.
- Aplicar esa idea al brillo de una imagen sin confundir la fórmula matemática con la representación de 8 bits.
## 1. Un píxel como número
Imagina una pequeña imagen en escala de grises. Cada píxel almacena una intensidad: valores bajos se ven oscuros y valores altos se ven claros. En una representación frecuente de **8 bits sin signo**, cada intensidad es un entero entre **0 y 255**. Este intervalo corresponde a esa representación concreta; no es una regla universal para todas las imágenes.
Por ejemplo, una fila de cuatro píxeles podría ser:
```plain text
[0, 40, 120, 255]
```
El primero es negro, el último es blanco y los otros dos son tonos intermedios. Todavía no necesitamos una cámara ni una red neuronal: basta con pensar en números.
## 2. Números y variables
`40` es un número concreto. La letra `x` es una **variable**: un símbolo cuyo valor puede cambiar. Si escribimos `x = 40`, hemos asignado a `x` un valor para este ejemplo. Después podemos estudiar la misma regla con `x = 120` sin reescribirla.
Una variable no tiene por sí sola un intervalo permitido. El contexto lo establece: si `x` representa una intensidad de 8 bits, entonces `x` debe ser un entero entre 0 y 255.
### Compruébalo a mano
Si una fila es `[0, 40, 120, 255]`, sustituye `x` por cada valor y calcula `x + 30`:
```plain text
[30, 70, 150, 285]
```
El último resultado es matemáticamente correcto, pero **285 no cabe en una intensidad de 8 bits**. Este detalle nos llevará a definir una función apropiada.
## 3. Una función es una regla
Una **función** asigna una salida a cada entrada permitida. Para aumentar el brillo de una intensidad de 8 bits en 30 unidades, podemos definir:
```plain text
f(x) = min(x + 30, 255)
```
`min(a, b)` selecciona el menor de los dos números. Así, cualquier resultado que supere 255 se limita a 255. A esta operación la llamaremos **recorte** o *clipping*.
<table header-row="true">
<tr>
<td>Entrada x</td>
<td>x + 30</td>
<td>Salida f(x)</td>
</tr>
<tr>
<td>0</td>
<td>30</td>
<td>30</td>
</tr>
<tr>
<td>40</td>
<td>70</td>
<td>70</td>
</tr>
<tr>
<td>120</td>
<td>150</td>
<td>150</td>
</tr>
<tr>
<td>255</td>
<td>285</td>
<td>255</td>
</tr>
</table>
Para este problema, el **dominio** de `f` es el conjunto de enteros `{0, 1, ..., 255}`: las entradas admitidas. Su **rango** es `{30, 31, ..., 255}`: las salidas que realmente puede producir. En particular, `f(225) = 255` y también `f(255) = 255`; entradas distintas pueden dar la misma salida.
### La idea visual
Una transformación de brillo se aplica a cada píxel de la imagen. Si la fila original es `[0, 40, 120, 255]`, la fila transformada es `[30, 70, 150, 255]`. La regla actúa sobre intensidades; todavía no cambia la posición de ningún píxel.
## 4. Primer ejemplo en Python
Puedes ejecutar este código en un intérprete de Python. No requiere bibliotecas externas.
```python
pixeles = [0, 40, 120, 255]

def aumentar_brillo(x, incremento=30):
    return min(x + incremento, 255)

resultado = [aumentar_brillo(x) for x in pixeles]
print(resultado)  # [30, 70, 150, 255]
```
`def` crea la función; `x` es su entrada y `return` entrega la salida. La última línea aplica la misma función a cada número de la lista.
Más adelante usaremos NumPy para operar con imágenes completas. Con arreglos de tipo `uint8` tendremos que convertir o limitar los valores cuidadosamente: la suma directa puede desbordarse antes del recorte.
## 5. Ejercicios
1. Calcula `f(10)`, `f(200)` y `f(240)` para `f(x) = min(x + 30, 255)`.
2. Define una regla `g(x)` que reduzca el brillo en 50 unidades sin producir valores negativos. Calcula `g(20)` y `g(120)`.
3. Explica por qué `x + 30` y `min(x + 30, 255)` son reglas distintas cuando `x = 240`.
4. Modifica el código para usar un incremento de 60. ¿Cuál es la salida para la fila `[0, 40, 120, 255]`?
5. Piensa en una imagen de 16 bits sin signo. ¿Seguiría siendo correcto limitar todas las salidas a 255? Explica tu respuesta.
## 6. Respuestas razonadas
1. `f(10) = 40`, `f(200) = 230` y `f(240) = 255`: la última suma da 270 y se recorta.
2. `g(x) = max(x - 50, 0)`. Por tanto, `g(20) = 0` y `g(120) = 70`.
3. La primera regla produce 270; la segunda produce 255. El recorte respeta el intervalo que elegimos para la imagen.
4. La nueva fila es `[60, 100, 180, 255]`.
5. No necesariamente. El límite depende de la representación y del significado de los datos; una imagen de 16 bits puede admitir valores superiores a 255.
## 7. Lo que sigue
En la próxima clase daremos una **posición** a cada intensidad. Con coordenadas `(fila, columna)` podremos explicar cómo se organiza una imagen y cómo representar sus valores en una gráfica. Esa idea será la base para hablar de matrices, filtros y detección de bordes.
**Recursos para profundizar**<br>**Gratuitos**<br>• [Khan Academy: introducción al álgebra](https://es.khanacademy.org/math/algebra-home) — empieza por la unidad «Introducción al álgebra».<br>• [OpenStax: funciones y notación](https://openstax.org/books/prec%C3%A1lculo-2ed/pages/1-1-funciones-y-notacion-de-funciones) y [dominio y rango](https://openstax.org/books/prec%C3%A1lculo-2ed/pages/1-2-dominio-y-rango) — lectura abierta en español.<br>• [Pillow: modos y bandas](https://pillow.readthedocs.io/en/stable/handbook/concepts.html) — documentación técnica (inglés).<br>**Libro comercial opcional**<br>• [Gonzalez y Woods, Digital Image Processing, 4.ª ed.](https://www.pearson.com/en-us/subject-catalog/p/Gonzalez-Digital-Image-Processing-4th-Edition/P200000003224/9780133356724) — consulta avanzada; no se requiere para esta clase.
