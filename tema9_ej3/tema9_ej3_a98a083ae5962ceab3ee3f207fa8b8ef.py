def decodificar(mensaje):
    mensaje=mensaje.split(",")
    i=0
    o=0
    while i < len(mensaje):
        new=int(mensaje[i], 2)
        mensaje[i]=new
        i+=1
    while o < len(mensaje):
        mensaje[o] = chr(mensaje[o])
        o += 1
    mensaje="".join(mensaje)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         