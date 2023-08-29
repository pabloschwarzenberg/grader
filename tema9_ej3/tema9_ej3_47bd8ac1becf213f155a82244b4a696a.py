def decodificar(mensaje):
    texto=[]
    mensaje=mensaje.split(",")
    suma=0
    for i in mensaje:
        suma=0
        u=128
        for k in i:
            if k=="0":
                u=u//2
            elif k=="1":
                suma+=u
                u=u//2     
        texto.append(chr(suma))
        mensaje="".join(texto)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         