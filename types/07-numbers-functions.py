""" Funciones de numeros"""

# Importamos el modulo de math: es un modulo que viene integrado con Python
import math

print(f"Retorna el numero mas cercano: {round(1.3)}")
print(f"Retorna el numero mas cercano: {round(1.7)}")
print(f"Retorna el valor siempre en positivo: {abs(-77)}")  # valor absoluto

# Uso de math

print(f"Retorna el numero entero superior mas cercano: {math.ceil(1.1)}")
print(f"Retorna el numero entero inferior mas cercano: {math.floor(1.999999)}")
print(f"Valida que sea un numero real: {math.isnan(1)}")
# eleva el primer valor por el segundo
print(f"Eleva un numero a la potencia: {math.pow(10, 3)}")
print(f"Retorna la raiz cuadrada: {math.sqrt(9)}")

# Documentacion de math: https://docs.python.org/3/library/math.html
