def decodificar(mensaje):
    mensaje=mensaje.split(",")
    mensaje_decodificado=""
    for i in mensaje:
        b=i
        n1=int(str(b),2)
        mensaje_decodificado=mensaje_decodificado+chr(n1)
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         