def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    mensaje_decodificado = ""

    for num_binario in numeros_binarios:
        num_decimal = int(num_binario, 2)
        letra = chr(num_decimal)
        mensaje_decodificado += letra

    return mensaje_decodificado
