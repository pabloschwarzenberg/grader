def suma_divisores(n):
    divisores=[]
    for i in range(1,n+1):
        if n % i == 0:
            divisores.append(i)
    suma=0
    for e in divisores:
        suma=suma+e
    suma=suma-divisores[-1]
    if suma==1:
        return(suma,True)
    else:
        return(suma,False)