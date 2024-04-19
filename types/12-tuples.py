""" Tuplas """

"""
Es una colección ordenada e inmutable
Es util cuando necesitas una lista ordenada pero que no sera modificada
"""

my_tuple = ('1', '2')

# desempaquetar tuples
"""
Se pueden crear funciones complejas, con los datos de las tuplas
"""

# lista de tuplas
print("Cree un software para entrar descuentos dependiendo el cliente")
print("\n")
coffe_db = [("Espresso", 2.5), ("Latte", 3.0), ("Cappuccino", 3.2)]
coffe_client = "Espresso"
discount_db = [("Family", 0.20), ("Regular", 0.12)]

name_client = input("Inserte el nombre del cliente: \n")

discount_client = input("Ingrese el tipo de cliente ['Famyl' o 'Regular']: \n")


def coffe_discount(coffe_client, coffe_list, discount_user_type, discount_db):
    discount_value = 0
    coffe_price = 0
    for coffe, price in coffe_list:
        if (coffe.lower() == coffe_client.lower()):
            coffe_price = price
        else:
            pass
    for name, dis in discount_db:
        if (name.lower() == discount_user_type.lower()):
            discount_value = dis
        else:
            pass
    total = coffe_price - discount_value
    print(f"""Hola!, {name_client}, eres parte de nuestro descuento {discount_user_type.capitalize()}
                Gracias por tu compra!                      CAFE {coffe_client}: ${round(total)}
        """)


coffe_discount(coffe_client, coffe_db, discount_client, discount_db)
