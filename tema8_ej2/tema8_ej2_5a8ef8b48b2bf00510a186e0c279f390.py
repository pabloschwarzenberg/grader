def buscarTodas(a,b):
    indice=[]
    i=0
    for r in a:
        if a[i] == b:
            indice.append(str(i))
        i+=1
    lista = " ".join(indice)
    return lista