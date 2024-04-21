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
    # Comenzamos con una lista que contiene el número primo más pequeño: 2.
    primos = [2]
    # Iniciamos nuestro contador en 3, ya que 0 y 1 no son primos, y el 2 ya está en nuestra lista.
    contador = 3

    if num < 2:  # Si el número ingresado es menor que 2, no hay primos.
        return 0

    # Creamos un bucle mientras el contador sea menor o igual al número ingresado.
    while contador <= num:
        """
        Creamos un bucle que recorre los números impares desde 3 hasta justo antes de contador,
        con un paso de 2, para verificar si contador es divisible por alguno de estos números.
        """
        for n in range(3, contador, 2):
            if contador % n == 0:  # Si contador es divisible por n, no es primo.
                contador += 2  # Pasamos al siguiente número impar.
                break
        else:
            # Si el bucle for se completa sin encontrar divisores, añadimos contador a la lista de primos.
            primos.append(contador)
            contador += 2  # Pasamos al siguiente número impar.

    print(primos)  # Imprimimos la lista de primos encontrados.
    return len(primos)  # Devolvemos la cantidad de números primos encontrados.


print(contar_primos(1))
