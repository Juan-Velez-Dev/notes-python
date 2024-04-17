""" Set """

"""
Es un conjunto desordenado y mutable de elementos unicos
Es util cuando se necesita eliminar elementos duplicados
Es desordenada y es no indexado, osea que no se puede acceder por medio del incice
"""

# sintaxis

my_set = set((1, 2, 3))

other_set = {1, 2, 3}

# union de sets

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

# agregar

s1.add(4)

# eliminar

s3.remove(3)

# descartar

# simplemente descarta entonces no genera ningun error si no encuentra el valor
s3.discard(6)

# limbiar el set

s1.clear()
