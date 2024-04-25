"""
Funciones que se reutilizan en todo el algoritmo
"""
from os import system


def command_user():
    while True:
        user_command = input("\nComando: ")
        if not user_command.isnumeric():
            if user_command.strip() == 'clear':
                system("clear")
            else:
                print("Los comandos deben ser números enteros.")
        else:
            return int(user_command)
