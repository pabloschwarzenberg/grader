def buscarTodas(a,b):
    y=[i for i,x in enumerate(a) if x==b]
    c=list(y)
    l=[]
    for i in c:
        l.append(str(i))
        x=" ".join(l)
    
    return x
