def buscarTodas(a,b):
    c=list(a)
    cc=""
    for i in range(len(a)):
        if c[i]==b:
            cc=cc+str(i)+" "
    return cc[:-1]