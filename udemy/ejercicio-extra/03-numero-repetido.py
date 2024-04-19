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
    cuenta = 0
    for numero in args:
        if numero == 0:
            cuenta += 1
        else:
            pass
    if cuenta > 2:
        return False
    else:
        return True


print(numero_repetido(5, 6, 1, 0, 0, 9, 3, 5))
print(numero_repetido(6, 0, 5, 1, 0, 3, 0, 1))
