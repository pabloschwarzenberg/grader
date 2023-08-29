def buscarTodas(a,b):
    posiciones = []
    inicio = 0
    hay = True
    while hay:
        posicion = a.find(b, inicio, len(a))
        if posicion != -1:
            posiciones.append(str(posicion))
            inicio = posicion+1
        else:
            hay = False
    sposiciones = ' '.join(posiciones)
    return sposiciones