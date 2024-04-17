""" Diccionario """

"""
Es una coleccion desordenada y mutable de clave-valor
Es util cuando necesitas almacenar en pares clave-valor y se desea acceder rapidamente por claves
No tienen un orden predecible
"""

dict = {'c1': 'valor1', 'c2': 'valor2'}

result = dict['c1']
print(result)

# consulta

client = {'nombre': 'Juan', 'edad': 27, 'role': [
    'admin'], 'curses': {'js': True, 'py': False}}
response = (client['edad'])  # retorna el valor de la propiedad
print(response)

# busqueda en listas

print(client['curses']['js'])
print(client['role'][0])

# prueba: enviar la letra f en mayuscula

dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
# letter = dic['c2'][2]
print(dic['c2'][2].upper())

# agregar elementos

dic[3] = 'c3'
print(dic)
dic[3] = 'c'
print(dic)

# claves

print(dic.keys())

# valores

print(dic.values())

# items

print(dic.items())
