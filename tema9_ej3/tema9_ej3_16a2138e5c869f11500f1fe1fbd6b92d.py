def decodificar(mensaje):
    # Dividir el mensaje en una lista de números binarios
    numeros_binarios = mensaje.split(',')

    # Convertir cada número binario a su equivalente decimal
    numeros_decimales = [int(num, 2) for num in numeros_binarios]

    # Convertir cada número decimal en su letra o símbolo correspondiente
    letras = [chr(decimal) for decimal in numeros_decimales]

    # Unir las letras y retornar el resultado
    mensaje_decodificado = ''.join(letras)
    return mensaje_decodificado
