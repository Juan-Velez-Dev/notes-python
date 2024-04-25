""" Escribir un archivo """

archivo = open("doc.txt", "w")
archivo = open("doc.txt", "r")
archivo = open("doc.txt", "a")
archivo.write("Soy el nuevo texto")
archivo.writelines(["Hola", "Mundo"])
archivo.close()
