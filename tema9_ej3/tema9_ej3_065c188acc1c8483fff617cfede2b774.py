def decodificar(mensaje):
    # Dividir el mensaje en una lista de números binarios separados por comas
    numeros_binarios = mensaje.split(",")

    # Convertir cada número binario a decimal y luego a su correspondiente letra
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]

    # Unir las letras para formar el mensaje descifrado
    mensaje_descifrado = "".join(letras)

    return mensaje_descifrado
