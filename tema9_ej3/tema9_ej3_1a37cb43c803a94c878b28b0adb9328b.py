def decodificar(mensaje):
    # Separar los números binarios y convertirlos a su equivalente decimal
    numeros = mensaje.split(",")
    decimales = [int(num, 2) for num in numeros]

    # Convertir los decimales a su representación de ASCII
    letras = [chr(decimal) for decimal in decimales]

    # Unir las letras y retornarlas como un string
    mensaje_decodificado = "".join(letras)
    return mensaje_decodificado
