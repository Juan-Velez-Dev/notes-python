""" Bucle While """

number = 1

while number < 100:  # siempre que se cumpla la condicion continua con la operacion
    print(number)
    number *= 2

comand = ""

while comand.lower() != "exit":
    comand = input("$ ")
    print(comand)

# Loop infinito

while True:
    comand = input("$ ")
    print(comand)
    if comand.lower() != "exit":
        break  # si es un loop infitinito siempre agregar una condicion de salida
