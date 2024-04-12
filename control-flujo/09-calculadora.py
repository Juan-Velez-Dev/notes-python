""" Calculadora """


print(f"""
        Bienvenido a mi calculadora
        las operaciones son con los comandos
        sum, res, mult
      """)

operation = ''
comand = ""
num = 0

while comand != 'exit':
    if num == 0:
        print('escribe el primer numero')
        num = input('$ ')
        if num == 'exit':
            break
        else:
            num = int(num)
    else:
        print('escribe el segundo numero')
        num2 = input('$ ')
        if num2 == 'exit':
            break
        else:
            num2 = int(num2)
            print('escribe el comando de operacion')
            operation = input('$ ')
            if operation == 'exit':
                break
            elif operation == 'sum' or operation == 'res' or operation == 'mult':
                if operation == 'sum':
                    print(f'El resultado de la suma es: {num + num2} ')
                    num = num + num2
                elif operation == 'res':
                    print(f'El resultado de la resta es: {num - num2}')
                    num = num - num2
                elif operation == 'mult':
                    print(f'El resultado de la multiplicacion es: {
                          num * num2}')
                    num = num * num2
            else:
                print('acceda un comando valido')
