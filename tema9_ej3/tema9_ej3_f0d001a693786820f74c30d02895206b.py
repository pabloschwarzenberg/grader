def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    letras = []

    for binario in numeros_binarios:
        decimal = 0
        potencia = 7

        for bit in binario:
            if bit == "1":
                decimal += 2 ** potencia
            potencia -= 1

        letras.append(chr(decimal))

    return "".join(letras)
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         