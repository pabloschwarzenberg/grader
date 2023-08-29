def buscarTodas(a,b):
    n=""
    i=0
    while b in a:
        n=n+str(a.find(b)+i)+" "
        lista=list(a)
        lista.remove(b)
        a="".join(lista)
        i+=1
    n=n[0:len(n)-1]
    return n

if __name__ == "__main__":
    pass
           