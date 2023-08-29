def decodificar(mensaje):
    mensaje = mensaje.split(",")
    for i in range(0,len(mensaje)):
        mensaje[i] = int(str(mensaje[i]), 2)
        mensaje[i] = chr(mensaje[i])
    mensaje = "".join(mensaje)
    return mensaje


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
