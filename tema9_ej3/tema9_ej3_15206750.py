def decodificar(mensaje):
    nuevo_mensaje=""
    mensaje_l=mensaje.split(",")
    for i in range(len(mensaje_l)):
        mensaje_l[i]=chr(int(mensaje_l[i],2))
    for i in range(len(mensaje_l)):
        nuevo_mensaje = nuevo_mensaje + mensaje_l[i]
    mensaje=nuevo_mensaje
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)