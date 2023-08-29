def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    caracteres = []

    for numero_binario in numeros_binarios:
        numero_decimal = int(numero_binario, 2)
        caracter = chr(numero_decimal)
        caracteres.append(caracter)

    mensaje_decodificado = "".join(caracteres)
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
