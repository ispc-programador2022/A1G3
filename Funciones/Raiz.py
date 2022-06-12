from Funciones.ing2i import ing1i
from Funciones.ing2i import ing2i
import time

def raiz():
    print("Ingresar primero el indice de la raiz y luego el radical")
    time.sleep(2)
    indice = 1 / ing1i()
    raiz = ing2i() ** indice
    print("EL resultado de la raiz es: " + str(raiz))
    return raiz

raiz()
