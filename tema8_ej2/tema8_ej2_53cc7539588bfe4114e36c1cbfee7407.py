def buscarTodas(a,b):
    a=list(a)
    listo=[]
    for n in range(0,len(a)-1):
        if a[n]==b:
            listo.append(str(n))
    resultado=" ".join(listo)
    return resultado


if __name__ == "__main__":
    pass
           