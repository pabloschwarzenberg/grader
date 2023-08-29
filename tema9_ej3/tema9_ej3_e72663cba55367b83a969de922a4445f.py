def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]
    return "".join(letras)


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)  # hola