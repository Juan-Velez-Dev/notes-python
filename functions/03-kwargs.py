""" Keywords arguments """


def get_product(**datos):  # aqui usamos el doble asterisco
    # asi accedemos al valor de la propiedad indicacon el nombre de la propiedad en especifico
    print(datos["id"])
    print(datos)


# si usamos esta funcion debemos de pasar oblagotoriamente el nombre del parametro el cual queremos que sea asginado
get_product(id="34", name="Iphone", description="Iphone 15")
