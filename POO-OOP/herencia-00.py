""" Herencia y su orden"""


class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("Que tal")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()

print(Nieto.mro())  # el orden de herencia
