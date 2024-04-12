""" Metodos de strings """

animal = "chanCHito felIZ"

print(f"String en mayuscula: {animal.upper()}")
print(f"String en minuscula: {animal.lower()}")
print(f"Primera letra mayuscula: {animal.capitalize()}")
print(f"Primera letra de cada palabra mayuscula: {animal.title()}")
print(f"Elimina los espacios en blanco al inicio y al final del stringj: {
      animal.strip()}")  # Se usa tambien "lstrip()" y "rstrip()" para eliminar de un unico lado
print(f"Busca el indice del string que estamos buscando: {animal.find("CH")}")
print(f"Remplaza el primer parametro por el segundo: {
      animal.replace("CH", "xh")}")
print(f"Valida si se encuentra el primer parametro en el segundo: {
      "fe" in animal}")  # Responde con un bool True or False

print(f"Valida si no se encuentra el primer parametro en el segundo: {
      "fe" not in animal}")  # Responde con un bool True or False
