def decodificar(mensaje):
    mensajef = ""
    mensaje1 = int(mensaje[0:8],2)
    mensaje2 = int(mensaje[9:17],2)
    mensaje3 = int(mensaje[18:26],2)
    mensaje4 = int(mensaje[27:],2)
    mensaje1 = chr(mensaje1)
    mensaje2 = chr(mensaje2)
    mensaje3 = chr(mensaje3)
    mensaje4 = chr(mensaje4)
    mensajef += (mensaje1 + mensaje2 + mensaje3 + mensaje4)
    return mensajef


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
