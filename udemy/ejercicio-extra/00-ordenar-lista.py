"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d','e','i','n','o','r','t']
"""


def ordenar_palabras(palabra):
    palabra_sin_repetidos = list(set(palabra))
    palabra_sin_repetidos.sort()
    return palabra_sin_repetidos


print(ordenar_palabras("entretenido"))
