def decodificar(mensaje):
    codigos_binarios = mensaje.split(',')
    letras = []
    for codigo_binario in codigos_binarios:
        numero_decimal = int(codigo_binario, 2)
        letra = chr(numero_decimal)
        letras.append(letra)
    mensaje_descifrado = ''.join(letras)
    return mensaje_descifrado

         