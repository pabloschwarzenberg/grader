def buscarTodas(a,b):

    palabra = a
    respuesta = ''
    posicion = 0
    posicion_ant = 0
    while palabra.find(b) >= 0:
        palabra.find(b) >= 0
        #print(palabra)
        posicion = palabra.find(b)
        #print(posicion)
        respuesta += str(posicion+posicion_ant) + ' '
        posicion_ant += posicion + 1
        palabra = palabra[posicion+len(b):]
    return respuesta[:len(respuesta)-1]