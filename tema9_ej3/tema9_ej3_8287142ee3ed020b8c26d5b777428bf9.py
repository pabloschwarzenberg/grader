def decodificar(mensaje):
    # Dividir el mensaje en una lista de números binarios
    numeros_binarios = mensaje.split(',')

    # Convertir cada número binario a decimal y luego a su correspondiente letra
    letras = [chr(int(num_binario, 2)) for num_binario in numeros_binarios]

    # Unir las letras para formar el mensaje descifrado
    mensaje_descifrado = ''.join(letras)

    return mensaje_descifrado

mensaje_cifrado = "01101000,01101111,01101100,01100001"
mensaje_descifrado = decodificar(mensaje_cifrado)
print(mensaje_descifrado)  # Salida: hola

