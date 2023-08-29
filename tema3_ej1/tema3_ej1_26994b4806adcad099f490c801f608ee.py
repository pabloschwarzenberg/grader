def suma_divisores(a):
    lista=[]
    n=0
    for x in range(1,a):
        if a%x==0:
            n=n+x
            lista.append(x)
    if len(lista)==1:
        x=True
    else:
        x=False
    return n,x