def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    letras = []
    for binario in numeros_binarios:
        decimal = int(binario, 2)
        letra = chr(decimal)
        letras.append(letra)
    mensaje_descifrado = "".join(letras)
    return mensaje_descifrado

if __name__ == "__main__":
    mensaje_codificado = input("Ingrese el mensaje codificado: ")
    mensaje_descifrado = decodificar(mensaje_codificado)
    print("Mensaje descifrado:", mensaje_descifrado)
