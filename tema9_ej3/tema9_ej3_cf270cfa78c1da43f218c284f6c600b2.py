def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    mensaje_decodificado = ''

    for num_binario in numeros_binarios:
        num_decimal = int(num_binario, 2)
        letra = chr(num_decimal)
        mensaje_decodificado += letra

    return mensaje_decodificado


# Ejemplo de uso
mensaje_codificado = "01101000,01101111,01101100,01100001"
mensaje_decodificado = decodificar(mensaje_codificado)
print(mensaje_decodificado)  # hola
