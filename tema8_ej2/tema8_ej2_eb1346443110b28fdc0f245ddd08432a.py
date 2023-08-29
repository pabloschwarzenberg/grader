def buscarTodas(cadena, carac):
    inicio=0
    indice = inicio
    while indice < len(cadena):
        if cadena[indice] == carac:
            return indice
        indice += 1
    return -1