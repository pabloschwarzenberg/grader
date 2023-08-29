def buscarTodas(a, b):
    posiciones = ""
    listPalabra = list(a)
    indice = 0
    while indice < len(listPalabra):
        if listPalabra[indice] == b:
            posiciones += str(indice) + " "
        indice += 1
    return posiciones.strip()