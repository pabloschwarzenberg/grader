def decodificar(mensaje):

    decodificado = ''
    binarios = mensaje.split(',')

    for binario in binarios:
        numero_decimal = 0
        i = 0
        for num in binario[::-1]:
            numero_decimal += int(num) * 2 ** i
            i += 1

        decodificado += chr(numero_decimal)

    return decodificado


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         