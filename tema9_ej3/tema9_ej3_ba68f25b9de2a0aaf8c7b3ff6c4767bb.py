def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    caracteres = [chr(int(numero_binario, 2)) for numero_binario in numeros_binarios]
    mensaje_decodificado = "".join(caracteres)
    return mensaje_decodificado


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)  # hola
