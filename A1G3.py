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
from Funciones.function_p1_9 import function_p1_9
from Funciones.function_p1_10 import function_p1_10
from Funciones.function_p1_11 import function_p1_11
from Funciones.function_genrnd_12 import genrnd
from Funciones.FunctionSumRandList import sumRandList 
from Funciones.FunctionProdRandList import prodRandList 
from Funciones.FunctionDivRandList import divRandList 

import time

#instancias de objetos
inicio = Presentation()
valores = FunctionIng2()

timeApp=[]


#presentacion
inicio.presentacion()

# punto 1
print("== Punto 1 ==")
lista = valores.ing2i()
valores.ing2s()
inicio = time.time()
FunctionSuma.printSuma(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 2
print("\n== Punto 2 ==")
inicio = time.time()
FunctionResta.printResta(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 3
print("\n== Punto 3 ==")
inicio = time.time()
FunctionProducto.printProducto(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 4
print("\n== Punto 4 ==")
inicio = time.time()
FunctionCociente.printCociente(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 5
print("\n== Punto 5 ==")
inicio = time.time()
FunctionModulo.printModulo(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 6
print("\n== Punto 6 ==")
inicio = time.time()
FunctionPotencia.printPotencia(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 7
print("\n== Punto 7 ==")
inicio = time.time()
FunctionRaiz.printRaiz(lista)
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 8
print("\n== Punto 8 no definido en la guia ==")
inicio = time.time()
fin = time.time()
timeApp.append([inicio,fin])

#punto 9
print("\n== Punto 9 ==")
inicio = time.time()
num = float(input("Ingrese un numero: " ))
print("El resultado es: ", function_p1_9(lista, num))
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 10
print("\n== Punto 10 ==")
inicio = time.time()
print("El resultado es: ", function_p1_10(lista, num))
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 11
print("\n== Punto 11 ==")
inicio = time.time()
print("El resultado es: ", function_p1_11(lista, num))
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 12
print("\n== Punto 12 ==")
inicio = time.time()
lista = genrnd(50,999)
print("Lista generada: ")

for k in range(len(lista)):
    if k % 10 == 0:
        print('\n')
    print(lista[k],end="   ")
print("\n")
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 13
print("\n== Punto 13 ==")
lstsum=sumRandList(lista)
print("Sumatoria de la lista: ")
for k in range(len(lstsum)):
    if k % 5 == 0:
        print('\n')
    print(lstsum[k],end="   ")
print("\n")
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])

#punto 14
print("\n== Punto 14 ==")
lstprod=prodRandList(lista)
print("Producto de la lista: ")
for k in range(len(lstprod)):
    if k % 5 == 0:
        print('\n')
    print(lstprod[k],end="   ")
print("\n")
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])


#punto 15
print("\n== Punto 15 ==")
lstdiv=divRandList(lista)
print("Cociente de la lista: ")
for k in range(len(lstdiv)):
    if k % 5 == 0:
        print('\n')
    print(lstdiv[k],end="   ")
print("\n")
time.sleep(1)
fin = time.time()
timeApp.append([inicio,fin])





#tiempo de ejecucion para separar en nueva funcion...
print('\n' * 3)
print("Tiempos de ejecucion")
act=1
for i in timeApp:
    print('Punto ', act ,': ', i[1]-i[0])
    act+=1
