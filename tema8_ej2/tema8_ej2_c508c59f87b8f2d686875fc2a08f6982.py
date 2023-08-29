def buscarTodas(a,b):
    indice=0
    c=[]
    d=" "
    while indice<len(a):
        indice_letra=a[indice]
        if indice_letra==b:
            c=c+list(str(indice))+list(d)
        indice+=1
    del c[-1]
    c="".join(c)
    return c

if __name__ == "__main__":
    pass
           