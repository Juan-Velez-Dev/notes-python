"""
Funciones generadoras
"""


def mi_generador():
    for x in range(1, 5):
        yield x * 10


g = mi_generador()

print(next(g))
print(next(g))
