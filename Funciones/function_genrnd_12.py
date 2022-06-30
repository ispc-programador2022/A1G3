from random import randint 

#funcion con 2 parámetros, el primero es ka cantidad de nuemros que quiero
#el segundo es la cantidad de numeros que van a entrar al metodo randint
def genrnd (cantidadNumerosAleatorios:int, cantidadNumerosRandint:int):

    listaAleatoria = [] # lista vacia para agregar los numeros
    contador = 0 # contador que cuenta las veces que se agrega un numero a la lista

    #se hace un while para que no se pase ni falten numeros en nuestra lista
    while contador < cantidadNumerosAleatorios:
        numeroAleatorio = randint(0,cantidadNumerosRandint) # randint genera numeros aleatorio, aqui generamos desde el 0 hasta el que elijan 
        if numeroAleatorio in listaAleatoria: # si el numeroAleatorio está en listaAleatorio entonces continua
            continue
        else: # si no agregalo a la listaAleatoria con un append
            listaAleatoria.append(numeroAleatorio) 
            contador = contador + 1 
    print(listaAleatoria)

genrnd(50,999999)