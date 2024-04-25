""" Analizador de texto """

print("Hola soy un software que se encarga de analizar y modificar el texto.")
print("""Este sofware puede contar, modificar, y hasta encontrar palabras claves
      
      1. Comenzamos primero contando cuantas veces aparecen nuestras letras seleccionadas en el texto:""")

user_text = input(f"Por favor añanade el texto que deseas analizar: ")

user_first_letter = input(f"Por favor ingrese la primera letra: ")
user_second_letter = input(f"Por favor ingrese la segunda letra: ")
user_third_letter = input(f"Por favor ingrese la tercera letra: ")

print(f"El texto que sera analizado es: \n{user_text}")
print(f"Tus letras son: {user_first_letter}, {
      user_second_letter}, {user_third_letter}")

cout_first_letter = user_text.lower().count(user_first_letter.lower())
cout_second_letter = user_text.lower().count(user_second_letter.lower())
cout_third_letter = user_text.lower().count(user_third_letter.lower())
print(cout_first_letter, cout_second_letter, cout_third_letter)

print(f"""El resultado es:
      La letra: {user_first_letter}, esta {cout_first_letter} veces.
      La letra: {user_second_letter}, esta {cout_second_letter} veces.
      La letra: {user_third_letter}, esta {cout_third_letter} veces.
      """)

print(f"2. Este es un contador de letras")
print(f"En el texto habian {len(list((user_text.strip())))} letras")

print("3. Tenemos un buscador de palabras asi que")

user_word_to_find = input("Escribe la palabra que desas buscar: ")

dic = {True: "si", False: "no"}
print(user_word_to_find.lower().strip() in user_text.lower())
print(f"La palabra ")
