def decodificar(a):
    a=a.split(",")
    print(a)
    d=0
    lista1=[]
    result=""
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            d=d*2+int(a[i][j])
        lista1.append(d)
        d=0
    for i in range(0,len(lista1)):
        z=chr(lista1[i])
        result=result+str(z)

    return result

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         