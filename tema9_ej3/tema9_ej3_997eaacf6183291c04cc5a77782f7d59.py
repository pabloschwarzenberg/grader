def decodificar(mensaje):
    R = []
    L = mensaje.split(",")
    for elem in L:
        R.append(chr(int(elem, 2)))
    respuesta = "".join(R)
    return respuesta