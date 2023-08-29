def decodificar(mensaje):
    mensaje = mensaje.split(",")
    for i in range(len(mensaje)):
        mensaje[i] = chr(int(mensaje[i],2))
    mensaje = ''.join(mensaje)
    return mensaje