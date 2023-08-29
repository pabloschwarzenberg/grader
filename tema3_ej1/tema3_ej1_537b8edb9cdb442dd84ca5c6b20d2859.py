def suma_divisores(a):
    l=[]
    b=int(a)
    i=1
    while a>i:
        if a%i==0:
            l.append(i)
            i=i+1
        else:
            i=i+1
    suma=sum(l)
    if a==1:
        return (0,False)
    if suma==1 and a>1:
        return (1,True)
    if suma!=0:
        return (suma,False)
           