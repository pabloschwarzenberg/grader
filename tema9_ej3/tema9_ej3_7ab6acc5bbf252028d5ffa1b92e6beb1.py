def decodificar(mensaje):
    mensaje=mensaje.split(",")
    mensaje1=[]
    string=""
    for i in mensaje:
        a=str(i)
        j=7
        h=0
        k=0
        while j>=0:
            c=int(a[j])*2**k
            j-=1
            k+=1
            h=h+c
        mensaje1.append(h)
    for i in mensaje1:
        string=string+chr(i)

    return string
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)