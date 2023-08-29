def buscarTodas(a,b):
    if b in a:
        indice=[]
        for i in range(0,len(a)):
            if a[i]==b:
                indice.append(str(i))
    indice=" ".join(indice)
    return indice
           