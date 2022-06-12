from Funciones.Presentacion import presentacion
from Funciones.Suma import suma
from Funciones.Resta import resta
from Funciones.Multiplicacion import multiplicacion
from Funciones.Division import division
from Funciones.Modulo import modulo
from Funciones.Potencia import potencia
from Funciones.Raiz import raiz


def operaciones():
    elegirO = input("¿Que operacion desea realizar? \n")

    if elegirO == "suma":
        suma()
    elif elegirO == "resta":
        resta()
    elif elegirO == "multiplicacion":
        multiplicacion()
    elif elegirO == "division":
        division()
    elif elegirO == "modulo":
        modulo()
    else:
        print("No ha señalado ninguna operacion")

presentacion()
operaciones()

