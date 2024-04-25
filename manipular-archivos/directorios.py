""" manipulacion de directorios """

import os
from pathlib import Path

# ruta = os.getcwd()
# ruta = os.chdir("C:\\Users\\juanv\\Documents\\code\\NOTES\\LANGUAJE\\PYTHON")
# ruta = os.makedirs(
#     "C:\\Users\\juanv\\Documents\\code\\NOTES\\LANGUAJE\\PYTHON\\Nueva-carpeta-con-python")
# archivo = open("otro_archivo.txt")
# print(archivo.read())

# print(ruta)

# ruta = "C:\\Users\\juanv\\Documents\\code\\NOTES\\LANGUAJE\\PYTHON\\Nueva-carpeta-con-python"
# elemento = os.path.basename(ruta)
# elemento = os.path.dirname(ruta)
# elemento = os.path.split(ruta)

# os.rmdir(ruta)
# print(elemento)

carpeta = Path("/Users/juanv/Documents/code/NOTES/LANGUAJE/PYTHON")
archivo = carpeta / 'otro_archivo.txt'
mi_archivo = open(archivo)
print(mi_archivo.read)
