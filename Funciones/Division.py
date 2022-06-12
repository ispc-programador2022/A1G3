from Funciones.ing2i import ing1i
from Funciones.ing2i import ing2i
import time

def division():
    print("Primero ingrese el dividendo y luego ingrese el divisor")
    time.sleep(2)
    division = ing1i() // ing2i()
    print("El resultado de la division es: " + str(division))
    return division
