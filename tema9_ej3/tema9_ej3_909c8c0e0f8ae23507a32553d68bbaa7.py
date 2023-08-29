def decodificar(mensaje):
    a=mensaje.split(",")
    mensajedec=[]
    x=0
    n=2
    while x < len(a):
        u=int(a[x], 2)
        k=chr(u)
        mensajedec.append(k)
        x+=1
    mensajedec="".join(mensajedec)
    return mensajedec

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         