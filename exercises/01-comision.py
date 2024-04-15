""" App para calcular comniciones"""

colaborate_name = input("Hola!, Bienvenido cual es tu nombre: ")
colaborate_sales = float(input("Cuanto fueron tus ventas este mes: "))
colaborate_comision = colaborate_sales * 13 / 100
print(f"Hola!, {colaborate_name}, tus ventas este mes fueron de : {colaborate_sales}, y tu comision del 13% fue: {
      colaborate_comision} eso nos da un total de {round(colaborate_sales + colaborate_comision, 2)}")
