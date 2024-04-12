""" Operadores logicos """

# and, or, not

gas = False
on = True
age = 18

if not gas and (on or age > 18):  # primero se evalua lo que esta dentro de los parentesis
    print("Puede pasar")

# Operador de corto circuito

if gas and on and age > 18:  # evalua que toda la evaluacion de True
    print("Puede pasar")

if gas or on or age > 18:  # evalua que alguna evaluacion sea True
    print("Puede pasar")
