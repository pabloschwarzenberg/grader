def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    letras = [chr(int(num, 2)) for num in numeros_binarios]
    return "".join(letras)

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
