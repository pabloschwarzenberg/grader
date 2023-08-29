def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    mensaje_decodificado = ''

    for binario in numeros_binarios:
        decimal = int(binario, 2)
        letra = chr(decimal)
        mensaje_decodificado += letra

    return mensaje_decodificado
         