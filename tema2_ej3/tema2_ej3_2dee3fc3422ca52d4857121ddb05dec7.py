def numero_perfecto(a):
    l=[]
    v=0
    k=""
    p=False
    for i in range(1,a+1):
        if (a%i==0 and i!=a):
            l.append(i)
    for x in l:
        v+=x
    if v==a:
        p=True
        return p
    return p