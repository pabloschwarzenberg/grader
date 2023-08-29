def decodificar(mensaje):
    divido = mensaje.split(,)
    frase = ""
    for divido in divido:
        numero = int(divido, 2)
        letra = chr(numero)
        frase += letra
    return frase

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
