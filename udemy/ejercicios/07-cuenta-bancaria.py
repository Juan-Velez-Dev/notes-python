""" Cuenta bancaria """


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellio, numero_cuenta, balance=0):
        super().__init__(nombre, apellio)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def depositar(self, value):
        self.balance += value
        print(f"Deposito aceptado ")

    def retirar(self, value):
        if self.balance >= value:
            self.balance -= value
            print("He retiro dinero")
        else:
            print("Fondos insuficientes")

    def __str__(self):
        return f"Hola {self.nombre} {self.apellido} en tu cuenta con el numero #{self.numero_cuenta} tienes {self.balance}"


def crear_cliente():
    nombre = input("Indica tu nombre : ")
    apellido = input("Indica tu apellido : ")
    numero_cuenta = input("Indica tu numero_cuenta : ")
    cliente = Cliente(nombre, apellido, numero_cuenta)
    return cliente


def inicio():
    print("Bienvenido a una app bancaria")
    cliente = crear_cliente()
    print(f"Cliente creado {cliente}")
    print("\n" + "*" * 20 + "\n")
    print("""
            Los comandos de la app son
          [1] : Depositar dinero
          [2] : Retirar dinero
          [3] : Salir de la app
        """)

    opcion = 0
    while opcion != 3:
        # print()
        opcion = int(input("Ingrese el comando : "))
        if opcion == 1:
            monto_dep = input("Cuanto desea depositar : ")
            cliente.depositar(int(monto_dep))
        elif opcion == 2:
            monto_dep = input("Cuato desea retirar : ")
            cliente.retirar(int(monto_dep))
        print(cliente)
    print("Gracias por operar con nosotrso")


inicio()
