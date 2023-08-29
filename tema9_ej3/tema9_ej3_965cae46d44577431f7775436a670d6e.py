
def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')  # Separar los números binarios por comas
    letras = []

    for numero_binario in numeros_binarios:
        numero_decimal = int(numero_binario, 2)  # Convertir el número binario a decimal
        letra = chr(numero_decimal)  # Obtener la letra o símbolo correspondiente al código ASCII
        letras.append(letra)

    mensaje_descifrado = ''.join(letras)  # Unir las letras en un solo mensaje

    return mensaje_descifrado
