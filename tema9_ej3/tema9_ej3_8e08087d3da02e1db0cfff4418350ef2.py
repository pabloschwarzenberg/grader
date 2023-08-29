def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    caracteres = []
    for binario in numeros_binarios:
        decimal = int(binario, 2)
        caracter = chr(decimal)
        caracteres.append(caracter)
    mensaje_descifrado = "".join(caracteres)
    return mensaje_descifrado

if __name__ == "__main__":
    mensaje_codificado = input("Ingrese el mensaje codificado: ")
    mensaje_descifrado = decodificar(mensaje_codificado)
    print("Mensaje descifrado:", mensaje_descifrado)

         