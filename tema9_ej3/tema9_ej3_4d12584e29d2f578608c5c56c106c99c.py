def decodificar(mensaje):
    # Separar los números binarios y convertirlos a decimal
    numeros_binarios = mensaje.split(",")
    numeros_decimales = [int(num, 2) for num in numeros_binarios]
    
    # Convertir los números decimales en letras
    letras = [chr(num) for num in numeros_decimales]
    
    # Unir las letras y retornar el mensaje descifrado
    mensaje_descifrado = "".join(letras)
    return mensaje_descifrado