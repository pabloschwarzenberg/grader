def buscarTodas(a,b):
    p=[i for i,x in enumerate(a) if x==b]
    o=list(p)
    u=[]
    for i in o:
        u.append(str(i))
        w=" ".join(u)
    return w