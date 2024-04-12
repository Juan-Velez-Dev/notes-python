""" Secuencia escape """

course = 'Ultimate "Python"'
print(f"Imprimiendo comillas dobles cuando usamos comillas simples: {course}")
course2 = "Ultimate \"Python\""  # Implementación de back slash
print(f"Imprimiendo comillas dobles cuando usamos comillas dobles: {course2}")
course3 = "Ultimate \\Python\""  # Implementación de back slash
print(f"Imprimiendo back slash: {course2}")
course3 = "Ultimate \nPython"  # Implementación de salto de linea
print(f"Imprimiendo el string con el salto de linea: {course3}")
