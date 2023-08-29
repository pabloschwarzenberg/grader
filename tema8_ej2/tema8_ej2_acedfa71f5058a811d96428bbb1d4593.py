def buscarTodas(a,b):
    palabrafinal=("")
    for i in range (len(a)):
        if a[i]==b:
            i=str(i)
            palabrafinal=palabrafinal+i+" "
    return str(palabrafinal)         