def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    mensaje_descifrado = ''

    for numero_binario in numeros_binarios:
        numero_decimal = int(numero_binario, 2)
        letra = chr(numero_decimal)
        mensaje_descifrado += letra

    return mensaje_descifrado

# Ejemplo de uso
mensaje_codificado = "01101000,01101111,01101100,01100001"
mensaje_descifrado = decodificar(mensaje_codificado)
print(mensaje_descifrado)  # Imprime "hola"
