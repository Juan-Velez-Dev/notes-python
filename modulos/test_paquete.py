from Paquete_Juan import suma_resta  # importacion de paquete
from Paquete_Juan.Sub_Paquete import saludo  # importacion de subpaquete

suma_resta.resta(12, 2)
suma_resta.resta(1, 4)

saludo.hola()  # se accede al subpaquete y luego a la funcion
