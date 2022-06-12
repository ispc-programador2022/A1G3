#imporamos las clases
#from Funciones.Presentacion import presentacion
from Funciones.Suma import suma
from Funciones.Resta import resta
from Funciones.Multiplicacion import multiplicacion
from Funciones.Division import division
from Funciones.Modulo import modulo
from Funciones.Potencia import potencia
from Funciones.Raiz import raiz

from Funciones.Presentacion import Presentation
from Funciones.FunctionIng2 import FunctionIng2
from Funciones.FunctionSuma import FunctionSuma
from Funciones.FunctionResta import FunctionResta
from Funciones.FunctionProducto import FunctionProducto
from Funciones.FunctionCociente import FunctionCociente
from Funciones.FunctionModulo import FunctionModulo
from Funciones.FunctionPotencia import FunctionPotencia
from Funciones.FunctionRaiz import FunctionRaiz
import time

#instancias de objetos
inicio = Presentation()
valores = FunctionIng2()

timeApp=[]


#presentacion
inicio.presentacion()
#punto 1
lista = valores.ing2i()
valores.ing2s()
inicio = time.time()
FunctionSuma.printSuma(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])
#punto 2
inicio = time.time()
FunctionResta.printResta(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])
#punto 3
inicio = time.time()
FunctionProducto.printProducto(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])
#punto 4
inicio = time.time()
FunctionCociente.printCociente(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])
#punto 5
inicio = time.time()
FunctionModulo.printModulo(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])
#punto 6
inicio = time.time()
FunctionPotencia.printPotencia(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])
#punto 7
inicio = time.time()
FunctionRaiz.printRaiz(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])





#tiempo de ejecucion para separar en nueva funcion...
print("Tiempos de ejecucion")
act=1
for i in timeApp:
    print('Punto ', act ,': ', i[1]-i[0])
    act+=1
