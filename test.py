from random import *

#  Lanzar dados


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"""La suma de tus dados es {suma_dados}. Lamentable"""
    elif suma_dados < 10:
        return f"""La suma de tus dados es {suma_dados}. Tienes buenas chances"""
    else:
        return f"""La suma de tus dados es {suma_dados}. Parece una jugada ganadora"""


resultado_dado1, resultado_dado2 = lanzar_dados()
mensaje = evaluar_jugada(resultado_dado1, resultado_dado2)
print(mensaje)

lista_numero = [1, 1, 1, 2, 65, 4, 3, 56, 76, 76, 3, 4]

# reudcir lista


def reducir_lista(lista):
    eliminar_duplicados = list(set(lista))
    eliminar_duplicados.remove(max(eliminar_duplicados))
    return eliminar_duplicados


def promedio(lista):
    return sum(lista) / len(lista)


resultado = promedio(reducir_lista(lista_numero))
print(resultado)

# moneda al azar


def lanzar_moneda():
    moneda = ['Cara', 'Cruz']
    return choice(moneda)


def probar_suerte(moneda: str, lista: list):
    if moneda.lower() == 'cara':
        lista = []
        print('La lista se autodestruirá')
        return lista
    else:
        print('La lista fue salvada')
        return lista


print(lanzar_moneda())
print(probar_suerte(lanzar_moneda(), [1, 2, 2, 1, 1, 2]))
