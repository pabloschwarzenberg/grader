def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = []

    for numero_binario in numeros_binarios:
        numero_decimal = int(numero_binario, 2)
        letra = chr(numero_decimal)
        letras.append(letra)

    mensaje_descifrado = ''.join(letras)
    return mensaje_descifrado

         