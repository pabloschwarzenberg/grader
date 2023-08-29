def buscarTodas (a,b):
    indexes=""
    for i in a:
        index=a.find(b)
        if index>=0:
            indexes+=str(index)+" "
        aL=list(a)
        aL[index]="0"
        a="".join(aL)
    return indexes[0:-1]