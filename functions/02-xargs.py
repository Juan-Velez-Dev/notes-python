""" Xargs """


def sum(*numbers):  # el "*" indica que nuestro parametro es iterable
    result = 0
    for number in numbers:
        result += number
    print(result)  # identamos el print por fuera del bucle for


sum(2, 3, 4, 1)
