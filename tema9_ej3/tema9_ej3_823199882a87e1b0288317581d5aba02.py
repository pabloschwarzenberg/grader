def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')  # Dividir el mensaje en números binarios separados por comas
    mensaje_decodificado = ''

    for binario in numeros_binarios:
        decimal = int(binario, 2)  # Convertir el número binario a decimal
        caracter = chr(decimal)  # Obtener el caracter correspondiente al código ASCII
        mensaje_decodificado += caracter  # Agregar el caracter al mensaje decodificado

    return mensaje_decodificado
