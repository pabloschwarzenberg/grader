def suma_divisores(a):
    l=[]
    v=0
    k=""
    p=False
    for i in range(1,a+1):
        if (a%i==0 and i!=a):
            l.append(i)
    if(len(l)==1):
        v=1
        p=True
        return v,p
    for x in l:
        v+=x
    return v,p