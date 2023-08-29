def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    letras = []
    
    for num_binario in numeros_binarios:
        num_decimal = int(num_binario, 2)
        letra = chr(num_decimal)
        letras.append(letra)
    
    mensaje_descifrado = "".join(letras)
    return mensaje_descifrado