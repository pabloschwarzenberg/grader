def decodificar(mensaje):
    # Separar los números binarios
    numeros_binarios = mensaje.split(',')

    # Convertir cada número binario a decimal y luego a su correspondiente carácter ASCII
    caracteres = [chr(int(binario, 2)) for binario in numeros_binarios]

    # Unir los caracteres y retornar el mensaje descifrado
    mensaje_descifrado = ''.join(caracteres)
    return mensaje_descifrado