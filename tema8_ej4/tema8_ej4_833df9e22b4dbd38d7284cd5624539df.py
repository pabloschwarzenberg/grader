def rot13(palabra):
    a=str("abcdefghijklmnopqrstuvwxyz")
    x=len(a)
    print(x)
    p=list(palabra.lower())
    lista=list(a)
    posiciones=[]
    for letra in p:
        i=0
        while i<len(lista):
            if lista[i]== letra:
                posiciones.append(i)
            i+=1
    cifrado=[]
    for elemento in posiciones:
        if elemento<13:
            cifrado.append(lista[elemento+13])
        else:
            cifrado.append(lista[elemento-13])

    string=""
    for n in cifrado:
        string+=n
    return(string)

