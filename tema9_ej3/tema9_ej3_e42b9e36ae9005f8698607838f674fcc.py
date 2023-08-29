def decodificar(mensaje):
    letras = ''
    codiguitos = mensaje.split(",")
    for cerouno in codiguitos:
        letras += chr(int(cerouno, 2))
    return letras


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
