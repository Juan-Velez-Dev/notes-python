"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""


def numero_repetido(*args):
    index = 0
    for num in args:
        # validamos que nuestro indice se pueda comparar con el indice siguiente, en caso de que no haya indice siguiente termina la operacion
        if index + 1 == len(args):
            return False
        # validamos que el num en arg sea '0' y el que le sigue tambien sea '0'
        elif args[index] == 0 and args[index + 1] == 0:
            return True
        else:
            index += 1
    return False


print(numero_repetido(5, 6, 1, 0, 0, 9, 3, 5))
print(numero_repetido(6, 0, 5, 1, 0, 3, 0, 1))
