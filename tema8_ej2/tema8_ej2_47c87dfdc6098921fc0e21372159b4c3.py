def buscarTodas(a,b):
    n=len(a)
    lista=[]
    listaf=""
    for i in range(n):
        p=a[i]
        if p==b:
            lista.append(i)
    c=len(lista)
    for f in range(c):
        p=lista[f]
        p=str(p)
        if f==(c-1):
            listaf=listaf+p
        else:
            listaf=listaf+p+" "
    return listaf

if __name__ == "__main__":
    pass
