def decodificar(mensaje):
    palabra = ''
    letras = int((len(mensaje)+1)/9)
    for j in range(letras):
        binario = mensaje[0:8]
        decimal = 0
        for i in range(len(binario)):
            numero = int(binario[i]) * 2 ** (len(binario) - i - 1)
            decimal += numero
        letra = chr(decimal)
        palabra += letra
        mensaje = mensaje.replace(mensaje[0:9], '')

    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         