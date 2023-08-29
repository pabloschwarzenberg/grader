def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")  # Separar los números binarios

    letras = []
    for binario in numeros_binarios:
        decimal = int(binario, 2)  # Convertir de binario a decimal
        letra = chr(decimal)  # Obtener la letra correspondiente al código ASCII
        letras.append(letra)

    mensaje_descifrado = "".join(letras)  # Unir las letras en un solo mensaje

    return mensaje_descifrado

if __name__ == "__main__":
    mensaje_cifrado = input("Ingrese el mensaje cifrado: ")

    mensaje_descifrado = decodificar(mensaje_cifrado)
    print(mensaje_descifrado)
