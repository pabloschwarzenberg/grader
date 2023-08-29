def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    numeros_decimales = [int(n, 2) for n in numeros_binarios]
    letras = [chr(n) for n in numeros_decimales]
    return "".join(letras)

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
