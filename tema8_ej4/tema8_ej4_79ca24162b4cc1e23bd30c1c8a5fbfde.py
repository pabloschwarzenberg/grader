def rot13(palabra):
    palabra.lower()
    n=len(palabra)
    lista1=("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    i=0
    lista2=[]
    n1=len(lista2)
    #separar el n como 1, 2, 3, 4
    while i<n and n!=n1:
        i+=1
        palabra.split(",")
        letra=str(palabra[i-1])
        b1=int(str.find(lista1,letra))

        if b1 != -1:
            a1=str(lista1[b1+13:b1+14])
            lista2.append(a1)
            cadena="".join(lista2)
    return cadena           