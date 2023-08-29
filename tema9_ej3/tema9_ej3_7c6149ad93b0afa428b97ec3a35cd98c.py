def decodificar(mensaje):
    binarios = mensaje.split(',')
    letter = []
    
    for b in binarios:
        d = int(b, 2)
        letra = chr(d)
        letter.append(letra)
    
    mensaje_descifrado = ''.join(letter)
    
    return mensaje_descifrado
