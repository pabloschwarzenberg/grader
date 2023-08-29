def decodificar(mensaje):
    mensaje = mensaje.split(",")
    i = 0
    decofificada = []
    while i < len(mensaje):
        n = int(mensaje[i], 2)
        decofificada.append(chr(n))
        i = i + 1
    return "".join(decofificada)



         