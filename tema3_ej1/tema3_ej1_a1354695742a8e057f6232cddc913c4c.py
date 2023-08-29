def suma_divisores(n):
    factores=[]
    for k in range(1,n):
            r=n%k
            if r==0:
                factores.append(k)
    a=sum(factores)
    if a==1:
        return a,True
        
    else:
        return a,False
           