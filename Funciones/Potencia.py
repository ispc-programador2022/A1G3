from ing2i import ing1i
from ing2i import ing2i
import time

def potencia():
    print("Primero ingrese la base de la potencia y luego ingrese el exponente")
    time.sleep(2)
    potencia = ing1i() ** ing2i()
    print("El resultado de modulo es: " + str(potencia))
    return potencia
