"""
Juego del Ahorcado
elejimos una palabra de una lista de palabras
programar las funciones que tendra el juego
"""

from random import *

# lista de nombres de mis mascotas y numero de vidas

pets_names = ['Homero', 'Berlin', 'Roma', 'Bruno', 'Waira', 'Gaia', 'Teodoro']
lifes = 10


"""
Funciones del Juego
"""


def random_name(pets_list):
    name = choice(pets_list)
    return "".join(name)


def hide_name(pet_name):
    new_name = ""
    for i in range(len(pet_name)):
        new_name += "_"
    return "".join(new_name)


def validator_char(char, pet_name):
    if char in pet_name:
        return True
    else:
        return False


def validator_name(pet_name, hidden_name):
    if pet_name == hidden_name:
        return True
    else:
        return False


def show_name(char: str, pet_name: str, hidden_name):
    new_hidden_name = list(hidden_name)
    for i in range(len(pet_name)):
        if char in pet_name[i]:
            new_hidden_name[i] = char
        else:
            new_hidden_name[i] = hidden_name[i]
    return "".join(new_hidden_name)


def game_over(pet_name):
    print(f"""
        Haz perdido, el nombre de mi mascota era :
            {pet_name}
            """)

# strat game


def start_game(lifes, list_names):
    input("Para comenzar presiona 'Enter' : ")
    pet_name = random_name(list_names).lower()
    hidden_name = hide_name(pet_name).lower()
    print(f"El nombre de mi mascota es : {" ".join(hidden_name)}")
    print(f"Comienzas con : {lifes} vidas\n")
    print("Cargando : *")
    print("Cargando : **")
    print("Cargando : ***")
    print("Cargando : ****")
    print("Cargando : *****")
    print("Cargando : ******")
    print("Cargando : *******")
    print("Cargando : ********")
    print("\n")
    print("\n")
    print("--------------------------------- START ---------------------------------")
    while lifes != 0:
        if validator_name(pet_name, hidden_name) == True:
            return print("\n!!!!!Felicidades haz Ganado!!!!!")
        print(pet_name)
        print(f"Vidas : {lifes} ❤")
        user_char = input("Ingresa una letra : ").lower()
        if validator_char(user_char, pet_name):
            hidden_name = show_name(user_char, pet_name, hidden_name)
            print(f"Haz acertado la letra !!! : {" ".join(hidden_name)}")
        else:
            lifes -= 1
    return game_over(pet_name)


start_game(lifes, pets_names)
