def buscarTodas(a,b):
     
    palabra=a
    posicion = 0
    posi_ant = 0
    resultado = ''
    while palabra.find(b) >= 0:
        palabra.find(b) >= 0
        posicion = palabra.find(b)
        resultado += str(posicion+posi_ant)+ ''
        posi_ant+= posicion + 1
        palabra = palabra[posicion+len(b):]
    return resultado[:len(resultado)+1]