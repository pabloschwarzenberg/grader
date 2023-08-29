def decodificar(mensaje):
    mensaje=mensaje.split(",")
    for n in range(len(mensaje)):
        mensaje[n]=int(mensaje[n])
        mensaje[n]=chr(mensaje[n])
    mensaje="".join(mensaje)
    return str(mensaje)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         