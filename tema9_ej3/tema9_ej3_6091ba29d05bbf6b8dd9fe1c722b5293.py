def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = [chr(int(numero_binario, 2)) for numero_binario in numeros_binarios]
    mensaje_decifrado = ''.join(letras)
    return mensaje_decifrado
         