def suma_divisores(a):
    n=1
    divisores=[]
    sumaDivisores=[]
    while n<a:
        if a%n==0:
            divisores.append(n)
        n=n+1
        divisores.sort()
    suma=0
    for i in divisores:
        suma=suma+i
    sumaDivisores.append(suma)
    if sumaDivisores[0]==1:
        sumaDivisores.append(True)
    else:
        sumaDivisores.append(False)
    resultado=(sumaDivisores[0],sumaDivisores[1])
    return(resultado)
