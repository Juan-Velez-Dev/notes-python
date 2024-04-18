""" Listas en Python"""

"""
Es una coleccion ordenada y mutable
Se usa cuando necesitas orden y quires modificar los elementos guardados
Las listas se distinguen por ser mutables
"""

my_list = ["e", "a", "c", "d", "b"]

# append: agrela el elmento al final de la lista

my_list.append('f')
print(my_list)

# pop: elimina el ultimo elemento al final de la lista, pero si pasamos por parametro el indice eliminarial el correspondiente al indice

my_list.pop()
print(my_list)

# sort: metodo de ordenamiento

my_list.sort()
print(my_list)

# comprension de listas: una letra por cada letra que haya en "Python"

letters_of_python = [letter for letter in "Python"]
print(letters_of_python)

# modificar antes de añadir a la lista: n divido 2 por cada n en el rango del 0 al 21, saltando de 2 en 2

numbers = [n / 2 for n in range(0, 21, 2)]
print(numbers)

# condicional: un n por cada n en el rango del 0 al 21, saltando de 2 en 2, siempre y cuando n multiplicado por 2 sea menor a 10

my_second_list = [n for n in range(0, 21, 2) if n * 2 > 10]

# if - else: un n siempre y cuando el resultado sea menor a 2, sino "no", por cada n en el rango

my_third_list = [n if n * 2 > 10 else "no" for n in range(0, 21, 2)]
