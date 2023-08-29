def numero_perfecto(n):
    factores=[]
    for k in range(1,n):
            r=n%k
            if r==0:
                factores.append(k)
    a=sum(factores)
    if a==n:
        return True
    else:
        return False
           