def decodificar(mensaje):
    # Separar los números binarios
    numeros_binarios = mensaje.split(',')

    # Convertir los números binarios a decimales y luego a caracteres
    caracteres = [chr(int(binario, 2)) for binario in numeros_binarios]

    # Unir los caracteres en un solo mensaje
    mensaje_descifrado = ''.join(caracteres)

    return mensaje_descifrado
