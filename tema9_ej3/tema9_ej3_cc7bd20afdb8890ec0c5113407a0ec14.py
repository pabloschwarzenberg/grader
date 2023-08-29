def decodificar(mensaje):
    mensaje = mensaje.split(",")
    lista = []
    for secuencia in mensaje:
        secuencia = (int(secuencia,2))
        secuencia = chr(secuencia)
        lista.append(secuencia)
    mensaje = "".join(lista)
    return mensaje                        
