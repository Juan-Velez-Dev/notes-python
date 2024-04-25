""" Path lib"""

from pathlib import Path, PureWindowsPath

carpeta = Path(
    "/Users/juanv/Documents/code/NOTES/LANGUAJE/PYTHON/otro_archivo.txt")

# para cambiar la ruta de Mac a Windows
# ruta_windows = PureWindowsPath(carpeta)

# print(carpeta.read_text())
# print(carpeta.read_text())

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia"))
print(guia.parent)
