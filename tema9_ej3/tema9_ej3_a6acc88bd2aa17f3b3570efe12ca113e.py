def decodificar(mensaje):
    lista=mensaje.split(",")
    msj=""
    for x in lista:
        msj+=chr(int(x[:8], 2))
    return msj

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         