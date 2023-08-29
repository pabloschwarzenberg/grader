def decodificar(mensaje):
    lista=mensaje.split(",")
    msj=""
    for x in lista:
        msj+=chr(int(x,2))
    return msj