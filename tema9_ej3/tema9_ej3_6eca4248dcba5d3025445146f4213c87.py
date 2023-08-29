def decodificar(z):
    lista1=[]
    lista2=[]

    for char in z:
        lista1.append(char)

    i=0
    while i<len(z):
        if z[i]==',':
            lista2.append(z[i-8:i])
        i=i+1
    if z.count(',')==len(z)//8 - 1:
        lista2.append(z[len(z)-8:])

    lista3=[]
    lista4=[]
    j=0
    while j<len(lista2):
        k=int(str(lista2[j]),2)
        m=chr(k)
        lista4.append(m)
        lista3.append(m)
        j=j+1

    return("".join(lista3))

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
         