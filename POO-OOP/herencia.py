""" Herencia """


class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):  # 'pajaro' hereda metodos y atributos de 'animal'}

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


perro = Animal(2, "yellow")

print(perro)


tucan = Pajaro(3, "yellow", 20)
