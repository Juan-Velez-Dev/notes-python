""" Clases en OOP """

# creamos la clase


class Pajaro:
    alas = True  # atributo de clase
    # cada vez que se cree una clase Python llama al construcor para ver que requisitos tiene la clase
    # self representa la instancia del objeto que vaya a ser creado

    def __init__(self, parametro, especie):  # metodo construcor de la clase
        self.atributo = parametro
        self.especie = especie

    def piar(self):
        print("pio, mi color es {}".format(self.atributo))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")

    """
    metodo de instancia:
    - accede y modifica atributos del objeto
    - accede a otros metodos
    - modica el estado de la clase
    """

    def pintar_negro(self):
        self.especie = "Guacamayo"
        self.piar()
        print(f"Ahora el pajaro es un {self.especie}")

    """
    metodo de clase

    """

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"puso {cantidad} huevos")
        cls.alas = False

    """
    
    """
    @staticmethod
    def mirar():
        print("El pajaro mira")


# instanciamos la clase
mi_pajaro = Pajaro("negro", "tucan")
print(mi_pajaro.especie)

print(type(mi_pajaro))

mi_pajaro.piar()

# metodos de instancia
Pajaro.poner_huevos(3)
