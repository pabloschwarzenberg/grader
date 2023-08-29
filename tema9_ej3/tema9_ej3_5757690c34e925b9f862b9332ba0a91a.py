def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]
    mensaje_descifrado = ''.join(letras)
    return mensaje_descifrado

mensaje_cifrado = "01101000,01101111,01101100,01100001"
mensaje_descifrado = decodificar(mensaje_cifrado)
print(mensaje_descifrado)  # hola
