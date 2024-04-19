"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
"""


def contar_primos(num):
    numeros = []
    if num == 0 or num == 1:
        return "El 0 y el 1 no son primos"
    while num < 0:
        if num % num == 0 and num % 1:
            numeros.append(num)
    return numeros


print(contar_primos(4))
