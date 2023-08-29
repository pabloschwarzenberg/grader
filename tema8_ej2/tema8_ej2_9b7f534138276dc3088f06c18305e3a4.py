def buscarTodas(a,b):
    a=str(a)
    b=str(b)
    lista_a=list(a)
    if b in a:
        m=len(lista_a)
        c=1
        n=-1
        p=[]
        while c<=m:
            n=a.find(b,n+1)
            if n==-1:
                break
            p.append(n)
            c=c+1
    lista=[]
    for i in range(len(p)):
        lista.append(str(p[i]))
    retorno=" ".join(lista)
    return retorno

if __name__ == "__main__":
    pass
           