def buscarTodas(a,b):
    lista=[]
    for x in range(len(a)):
        if a[x]==b:
            lista.append(str(x))
    return " ".join(lista)
