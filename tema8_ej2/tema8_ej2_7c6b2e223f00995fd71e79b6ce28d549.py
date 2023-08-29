def buscarTodas(a,b):
    i=0
    n=1
    x=a.count(b)
    posiciones=""
    for letra in a:
        if letra==b:
            if n<x:
                i=str(i)
                posiciones=posiciones+i+" "
                n=n+1
            elif n==x:
                i=str(i)
                posiciones=posiciones+i
        i=int(i)
        i=i+1
    return posiciones       