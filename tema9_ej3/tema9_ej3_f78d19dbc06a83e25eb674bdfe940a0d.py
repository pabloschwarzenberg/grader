def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = [chr(int(num, 2)) for num in numeros_binarios]
    mensaje_decodificado = ''.join(letras)
    return mensaje_decodificado