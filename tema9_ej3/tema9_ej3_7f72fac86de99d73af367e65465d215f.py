def decodificar(mensaje):
    mensaje=mensaje.split(",")
    mensajedec=""
    for elem in mensaje:
        elem=int(elem)
        elem=int(str(elem),2)
        elem=chr(elem)
        mensajedec+=elem
    mensaje=mensajedec
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         