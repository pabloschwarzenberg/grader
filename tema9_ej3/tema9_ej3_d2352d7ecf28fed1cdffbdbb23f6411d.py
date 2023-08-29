def decodificar(mensaje):
    a=mensaje.split(",")
    decodificado=""
    for i in range(len(a)):
        mini=chr(int(a[i],2))
        decodificado=decodificado+mini
    return decodificado

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         