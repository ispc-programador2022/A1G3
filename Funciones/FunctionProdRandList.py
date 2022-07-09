def prodRandList(listaAleatoria):
    producto = []

    for s in range(0,len(listaAleatoria),2):
        producto.append(str(listaAleatoria[s])+'x'+str(listaAleatoria[s+1])+'= '+str(listaAleatoria[s]*listaAleatoria[s+1]))
    
    return producto