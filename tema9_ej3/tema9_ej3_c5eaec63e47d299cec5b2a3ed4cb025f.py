def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')  # Separar los números binarios
    letras = []
    
    for binario in numeros_binarios:
        decimal = int(binario, 2)  # Convertir el número binario a decimal
        letra = chr(decimal)  # Obtener la letra correspondiente al código ASCII
        letras.append(letra)  # Agregar la letra a la lista
    
    mensaje_descifrado = ''.join(letras)  # Unir todas las letras en un solo mensaje
    
    return mensaje_descifrado


#respuesta
mensaje_cifrado = "01101000,01101111,01101100,01100001"
mensaje_descifrado = decodificar(mensaje_cifrado)
print(mensaje_descifrado)

         