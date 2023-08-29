def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    caracteres = [chr(int(num_binario, 2)) for num_binario in numeros_binarios]
    mensaje_descifrado = ''.join(caracteres)
    return mensaje_descifrado
