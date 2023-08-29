def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    mensaje_decodificado = ""

    for binario in numeros_binarios:
        decimal = int(binario, 2)
        caracter = chr(decimal)
        mensaje_decodificado += caracter

    return mensaje_decodificado
