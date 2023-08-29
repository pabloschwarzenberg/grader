def suma_divisores(a):
    a=int(a)
    p=[]
    for i in range(1,10):
        if a%i==0 and i!=a:
            p.append(i)
    if a==1:
        return 0,False
    if sum(p)==1 and a!=1:
        return sum(p),True
    elif sum(p)!=1:
        return sum(p),False