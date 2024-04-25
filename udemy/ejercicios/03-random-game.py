""" Juego de adivinanza de numero aleatorios """
from random import *
print("¡Hola!, soy un juego interactivo echo por: JuanDev \n Mi nombre es RandomNeitor-01.02")
user_name = input("Cual es tu nombre: ")
print("\n")
print(f"""Bueno, {user_name}, he construido un sript que eliminara lo mas importante de tu computador.
      Para desactivarlo tendras que adivinar un numero entre el 1 y el 100.
      Piensalo muy bien porque solo tienes 8 intentos""")

secret_number = randint(1, 101)
number_of_tries = 8

print("\n")

while number_of_tries > 0:
    number_of_tries -= 1
    user_number = int(
        input("ingresa un numero!, (Recuerdad entre el 1 y el 100): "))
    print("\n")
    if (number_of_tries == 0):
        print("Perdiste, haz agotado el numero de intentos!")
        print("\n")
    elif (user_number < 1 or user_number > 100):
        print(f"""¡Haz ingresado un numero menor que 1 o mayor que 100!
              perdiste un intento, ahora solo tienes: {number_of_tries}""")
    elif (user_number < secret_number):
        print(f"""¡Haz ingresado un numero menor al numero secreto!
              perdiste un intento, ahora solo tienes: {number_of_tries}""")
        print("\n")
    elif (user_number > secret_number):
        print(f"""¡Haz ingresado un numero mayor al numero secreto!
              perdiste un intento, ahora solo tienes: {number_of_tries}""")
        print("\n")
    elif (user_number == secret_number):
        print(f"""Haz acertado el numero secreto, era {secret_number}
              Y lo lograste en: {number_of_tries} intentos""")
        print("\n")
        break
