"""
Porgrama de gestion de recetas
Este codigo es del curso de Udemy
"""

import os
from pathlib import Path
from os import system


mi_ruta = Path(Path.home(),
               "Documents/code/NOTES/LANGUAJE/PYTHON/udemy/ejercicios/Receta/Recetas")


def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def inicio():
    system('clear')
    print("*" * 50)
    print("*" * 5 + " Bienvenido al administrador de recetas " + "*" * 5)
    print("*" * 50)
    print("\n")
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'  # este valor es para que el bucle se repita
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("Elije una opcion")
        print("""
            [1] - Leer receta
            [2] - Crear receta nueva
            [3] - Crear categoria nueva
            [4] - Eliminar receta
            [6] - Salir del programa
            """)
        eleccion_menu = input("")
    return int(eleccion_menu)


def mostrar_categorias(ruta):
    print("Categorias")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias


def elegir_categoria(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\n elige una categoria : ")
    # se resta 1 para comenzar en el indice correcto
    return lista[int(eleccion_correcta) - 1]

    # Mostrar menu de inicio


def mostrar_recetas(ruta):
    print("Recetas : ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("**/*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta_str)
        contador += 1
    return lista_recetas


def elegir_recetas(lista):
    eleccion_receta = "x"
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\n Elegir receta :")
    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta : ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print("Tu receta ha sido creada")
            existe = True
        else:
            print("Lo siento esta receta ya existe")


def crear_cateogira(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu categoria")
        nombre_categoria = input() + ".txt"
        print("Escribe tu nueva cateogira : ")
        contenido_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
    if not os.path.exists(ruta_nueva):
        Path.mkdir(ruta_nueva)
        print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
        existe = True
    else:
        print("Lo siento la categoria ya existe")


def eliminar_receta(receta):
    Path(receta).unlink()
    print("La receta ha sido eliminada")


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print("Se ha eliminado la categoria ")


def volver_inicio():
    eleccion_regresar = "x"
    while elegir_categoria.lower() != "v":
        eleccion_regresar = input("\nPresiona V para volver al menu")


finalizar_programa = False

while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # eligir categorias
        mi_categoria = elegir_categoria(mis_categorias)
        # mostrar recetas
        mis_recetas = mostrar_recetas(mi_ruta)
        # elegir receta
        mi_receta = elegir_categoria(mis_recetas)
        # leer receta
        leer_receta(mi_receta)
        # volver inicio
        volver_inicio()

    elif menu == 2:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # crear receta nueva
        crear_receta(mi_ruta)
        # volver inicio
        volver_inicio()

    elif menu == 3:
        mis_categorias = mostrar_categorias(mi_ruta)
        # crear categoria
        crear_cateogira(mis_categorias)
        # volver inicio
        volver_inicio()

    elif menu == 4:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # eligir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # mostrar recetas
        mis_recetas = mostrar_recetas(mi_ruta)
        # elegir receta
        mi_receta = elegir_categoria(mis_recetas)
        # eliminar receta
        eliminar_receta(mi_receta)
        # volver inicio
        volver_inicio()

    elif menu == 5:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # eliminar categoria
        eliminar_categoria(mi_categoria)
        # volver inicio
    elif menu == 6:
        # finalizar programa
        finalizar_programa = True
