""" Manipulando archivos """

mi_archivo = open("doc.txt")

# print(mi_archivo.read())
print(mi_archivo.readline())
for i in mi_archivo:
    print("Aqui dice: " + i)

# todas = mi_archivo.readlines()

mi_archivo.close()
