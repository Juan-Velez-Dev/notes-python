def decorar_funciones(function):
    def otra_funcion(palabra):
        print("Hola")
        function(palabra)
        print("Adios")
    return otra_funcion


def mayusculas(palabra):
    print(palabra.upper())


def minuscula(palabra):
    print(palabra.lower())


mayuscula_decorada = decorar_funciones(mayusculas)
mayuscula_decorada("Hola")
