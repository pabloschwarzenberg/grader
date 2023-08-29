def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    mensaje_descifrado = ""

    for numero_binario in numeros_binarios:
        numero_decimal = int(numero_binario, 2)
        caracter = chr(numero_decimal)
        mensaje_descifrado += caracter

    return mensaje_descifrado
