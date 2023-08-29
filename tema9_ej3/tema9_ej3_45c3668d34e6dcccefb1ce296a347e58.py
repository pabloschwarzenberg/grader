def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = []
    
    for b in numeros_binarios:
        decimal = int(b, 2)
        letra = chr(decimal)
        letras.append(letra)
    
    mensaje_descifrado = ''.join(letras)
    
    return mensaje_descifrado
