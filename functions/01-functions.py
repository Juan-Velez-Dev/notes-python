""" Funciones """


def hello(name):  # el nombre de la variable dentro de la funcion es parametro
    print(f'Hello, {name}')


hello('Juan')  # lo que reibe que la funcion es argumento


# argumentos nombrados

def hello_user(name, role="user"):
    print(f'Hello, {name}, {role}')


hello_user('juan')  # lo que reibe que la funcion

hello_user(name='juan', role="admin")
