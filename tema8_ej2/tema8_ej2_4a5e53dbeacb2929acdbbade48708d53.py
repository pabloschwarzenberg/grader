def buscarTodas(a,b):
    lista=[]
    for g in range(0,len(a)):
        if (b==a[g]):
            lista.append(str(g))
    a=" ".join(lista)
    return(a)

if __name__ == "__main__":
    pass
           