def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")  # Separar los números binarios
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]  # Convertir los números binarios a caracteres
    mensaje_descifrado = "".join(letras)  # Unir las letras en un solo mensaje
    return mensaje_descifrado