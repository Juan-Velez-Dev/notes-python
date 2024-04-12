""" Strings """

course_name = 'Ultimate Python'
course_description = """
Ultimate Python,
este curso contempla todos los detalles que necesitas aprender.
"""
# Longitud del string
print(len(course_description))

# Acceder al index del string
print(course_name[2])

# Slice

print(course_name[2:5])  # slice del index 2 al 5
print(course_name[2:])  # slice a partir del index 2 hasta el final del string
print(course_name[:5])  # slice desde el comienzo del string hasta el index 5
print(course_name[:])  # Python devuelve todo el string
