def decodificar(mensaje):
    n = mensaje.split(",")
    str = ""
    for i in n:
        num = int(i, 2)
        letra = chr(num)
        str += letra
    return str
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)