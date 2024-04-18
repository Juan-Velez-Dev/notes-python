""" Diferentes caso condicionales """
serie = "N-02"

match serie:
    case "N1-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("iPhone")
    case _:
        print("No se reconoce")

cliente = {"nombre": "Juan",
           "edad": 27,
           "ocupacion": "programador"
           }

pelicula = {"titulo": "Matrix",
            "ficha_tecnica": {
                "protagonista": "Kenau reeves", "director": "Lana y Lilly"
            }
            }

elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "copacion": copacion}:
            print("Es un cliente")
            print(nombre, edad, copacion)
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista": protagonista,
                                "director": director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se reconoce el valor ingresado")
