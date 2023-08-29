def decodificar(mensaje):
    numeros_binarios = mensaje.split(',')
    mensaje_decodificado = ""

    for numero_binario in numeros_binarios:
        decimal = int(numero_binario, 2)
        letra = chr(decimal)
        mensaje_decodificado += letra

    return mensaje_decodificado


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
