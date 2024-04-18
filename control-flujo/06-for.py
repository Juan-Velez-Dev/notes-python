"""" Bucle for """

find_number = 3

for number in range(1, 5):  # range es uno de los mucho iterables de Python,
    if number == find_number:
        print("Econtrado", find_number)
        break  # se llama en caso de que no tengamos un for-else
else:
    print("No se encontro el numero")

for char in "Ultimate Python":
    print(char)  # imprime cada caracter del stirng
