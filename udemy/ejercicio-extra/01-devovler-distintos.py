"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valor intermedio.
"""


def devolver_distintos(*args):
    # cree una lista para darles su ordenamiento mas adelanta
    numeros = list(args)
    if sum(args) > 15:
        return max(args)
    elif sum(args) < 10:
        return min(args)
    else:
        # aqui ordenamos la lista para retornar el numero de valor intermedio entre los 3
        numeros.sort()
        return numeros[1]


print(devolver_distintos(13, 1, 1))
print(devolver_distintos(5, 6, 3))
