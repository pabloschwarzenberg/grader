def decodificar(mensaje):
    aux = mensaje.split(",")
    out = ""
    for char in aux:
        caracter = chr(int(char, 2))
        out += caracter
    return out


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
