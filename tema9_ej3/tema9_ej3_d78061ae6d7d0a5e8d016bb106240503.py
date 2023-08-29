def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    letras = []

    for numero_binario in numeros_binarios:
        numero_decimal = int(numero_binario, 2)
        letra = chr(numero_decimal)
        letras.append(letra)

    mensaje_descifrado = "".join(letras)
    return mensaje_descifrado
    
mensaje_codificado = "01101000,01101111,01101100,01100001"
mensaje_descifrado = decodificar(mensaje_codificado)
print(mensaje_descifrado)  # Resultado: "hola"


         