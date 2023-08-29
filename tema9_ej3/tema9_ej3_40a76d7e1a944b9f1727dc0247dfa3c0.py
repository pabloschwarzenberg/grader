def decodificar(mensaje):
    list_txt=mensaje.split(",")
    mensaje=""
    for i in list_txt:
        mensaje=mensaje+(chr(int(i,2)))
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)