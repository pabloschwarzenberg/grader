def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]
    mensaje_descifrado = "".join(letras)
    return mensaje_descifrado

if __name__ == "__main__":
    mensaje_cifrado = "01100001,01100010,01100011,01100100,01100101,01100110"
    resultado = decodificar(mensaje_cifrado)
    print("Mensaje descifrado:", resultado)
