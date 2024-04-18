""" Zip """

nombres = ['Rosita', 'Hugo', 'Valeria']
edades = [23, 32, 56]
ciudades = ["Lima", "Madrid", "Mexico"]

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre}, tiene {edad} y vive en {ciudad}")
