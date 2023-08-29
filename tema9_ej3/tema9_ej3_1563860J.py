def decodificar(mensaje):
    lista=[]
    lista2=[]
    string=""
    l=mensaje.split(",")
    for i in l:
        a=0
        for e in range(0,len(i)):
            n=int(i[e])*2**(len(i)-e-1)
            a=a+n
        lista.append(a)
    for i in lista:
        lista2.append(chr(i))
    string=string.join(lista2)
    return string

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         