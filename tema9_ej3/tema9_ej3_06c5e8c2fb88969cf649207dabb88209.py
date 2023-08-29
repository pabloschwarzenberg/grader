def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = [chr(int(num_binario, 2)) for num_binario in numeros_binarios]
    mensaje_decodificado = ''.join(letras)
    return mensaje_decodificado
