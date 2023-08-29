def suma_divisores(a):
    suma=0
    for k in range(1,a):
        if a%k==0:
            suma+=k
    if suma==1:
        return (suma,True)
    else:
        return (suma,False)
           