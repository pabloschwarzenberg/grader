def decodificar(mensaje):
    binarios = mensaje.split(",")
    mensaje = ""
    for binario in binarios:
        decimal = 0
        for x in range(len(binario)):
            decimal += int(binario[x])*(2**(len(binario)-x-1))
        mensaje += chr(decimal)
    return mensaje