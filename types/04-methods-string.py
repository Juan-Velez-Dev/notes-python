""" Metodos de strings """

animal = "chanCHito felIZ"

# UPPER
print(f"String en mayuscula: {animal.upper()}")
# LOWER
print(f"String en minuscula: {animal.lower()}")
# CAPITALIZE
print(f"Primera letra mayuscula: {animal.capitalize()}")
# TITLE
print(f"Primera letra de cada palabra mayuscula: {animal.title()}")
# STRIP
print(f"Elimina los espacios en blanco al inicio y al final del stringj: {
      animal.strip()}")  # Se usa tambien "lstrip()" y "rstrip()" para eliminar de un unico lado
# FIND
print(f"Busca el indice del string que estamos buscando: {animal.find("CH")}")
# REPLACE
print(f"Remplaza el primer parametro por el segundo: {
      animal.replace("CH", "xh")}")
# VALIDANDO PARAMETROS
print(f"Valida si se encuentra el primer parametro en el segundo: {
      "fe" in animal}")  # Responde con un bool True or False

print(f"Valida si no se encuentra el primer parametro en el segundo: {
      "fe" not in animal}")  # Responde con un bool True or False

# INDEX
text = "Hola mundo, mi nombre es Juan y tengo un amigo de nombre Ed"
# retorna el indice del primer caracter de la plabra encontrada
print(text.index("nombre"))
print(text.rindex("nombre"))
# retorna el indice del primer caracter encontrado
print(text.index("o"))

print(text[2])

# FIND
print(text.find("mundo"))

# REPLACE
print(text.replace("Hola", "Adios"))
