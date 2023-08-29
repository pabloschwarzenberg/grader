# completa el código de la función
def suma_divisores(a):
    indice = a
    suma_divisores = 0
    listaRespuesta = []
    while indice > 0:
        if a != indice:
            if a % indice == 0:
                suma_divisores += indice
        indice -= 1
    if suma_divisores == 1 or a == 1:
        listaRespuesta.append(suma_divisores)
        listaRespuesta.append(True)
    else:
        listaRespuesta.append(suma_divisores)
        listaRespuesta.append(False)

    return "("+str(listaRespuesta[0])+", "+str(listaRespuesta[1])+")"
