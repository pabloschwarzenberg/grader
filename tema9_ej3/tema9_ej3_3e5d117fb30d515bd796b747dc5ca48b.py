def decodificar(mensaje: str):
    msg = ''
    for i in mensaje.split(','):
        msg += chr(int(i, 2))
    return msg


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
