def sumRandList(listaAleatoria):
    sumatoria = []

    for s in range(0,len(listaAleatoria),2):
        sumatoria.append(str(listaAleatoria[s])+'+'+str(listaAleatoria[s+1])+'= '+str(listaAleatoria[s]+listaAleatoria[s+1]))
    
    return sumatoria