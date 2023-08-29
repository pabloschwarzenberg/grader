def decodificar(mensaje):
    mensaje = mensaje.split(",")
    palabra = ""
    for i in mensaje:
        c = int(str(i), 2)
        c = chr(c)
        palabra = palabra +c
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         