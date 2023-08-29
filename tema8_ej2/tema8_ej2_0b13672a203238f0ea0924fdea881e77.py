def buscarTodas(a,b):
    F=[i for i,x in enumerate(a) if x==b]
    Z=list(F)
    l=[]
    for i in Z:
        l.append(str(i))
        P = " ".join(l)
    return P