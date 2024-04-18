""" Libreria Random """

from random import *

aleatorio = randint(1, 50)
print(aleatorio)

decimal_aleatorio = round(uniform(1, 5), 1)
print(decimal_aleatorio)

numero_aleatorio = random()  # entrega un numero desde el 0 hasta el 1
print(numero_aleatorio)

# choice: string aleatorio

colores = ["azul", "rojo", "verde"]
color_aleatorio = choice(colores)
print(color_aleatorio)

# shuffle: hace una mezcla en los parametros que tenga
numeros = list(range(5, 50, 5))
shuffle(numeros)
print(numeros)
