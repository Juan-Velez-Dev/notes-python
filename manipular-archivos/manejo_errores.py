"""
Modulo de manejo de errores
"""


def suma():
    n1 = input("Escriba el primer numero")
    n2 = input("Escriba el segundo numero")
    print(n1 + n2)


try:
    # codigo que queremos probar
    suma()
except TypeError:
    # codido a ejecutar si hay un error
    print("Los tipos no coinciden")
except ValueError:
    print("Este no es un numero")
else:
    # codigo a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    # codigo a ejecutar de todos modos
    print("Eso fue todo")
