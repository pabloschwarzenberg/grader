def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]
    mensaje_decodificado = ''.join(letras)
    return mensaje_decodificado

     