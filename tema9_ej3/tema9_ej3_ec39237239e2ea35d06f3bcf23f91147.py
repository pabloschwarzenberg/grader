def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    caracteres = []

    for numero_binario in numeros_binarios:
        numero_decimal = int(numero_binario, 2)
        caracter = chr(numero_decimal)
        caracteres.append(caracter)

    mensaje_decodificado = "".join(caracteres)
    return mensaje_decodificado