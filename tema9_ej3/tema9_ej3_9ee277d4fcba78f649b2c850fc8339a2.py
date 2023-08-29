def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    letras = [chr(int(numero, 2)) for numero in numeros_binarios]
    mensaje_descifrado = "".join(letras)
    return mensaje_descifrado
