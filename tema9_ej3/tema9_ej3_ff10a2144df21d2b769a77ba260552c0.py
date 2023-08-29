def decodificar(mensaje):
    lista=mensaje.split(",")
    s=""
    for i in lista:
        dec=int(str(i), 2)
        s=s+chr(dec)       
    return s

if __name__ == "__main__":
    hola=int()
    mensaje="01101000,01101111,01101100,01100001"
    print(decodificar(mensaje))