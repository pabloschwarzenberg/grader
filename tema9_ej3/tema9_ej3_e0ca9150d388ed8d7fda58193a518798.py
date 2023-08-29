def decodificar(mensaje):
    traducido = ""
    splitted = mensaje.split(",")
    for binario in splitted:
        decimal = int(binario, 2)
        traducido = traducido + chr(decimal)
    return traducido

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)