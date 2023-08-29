def numero_perfecto(a):
    n=1
    divisores=[]
    while n<a:
        if a%n==0:
            divisores.append(n)
        n=n+1
        divisores.sort()
    suma=0
    for i in divisores:
        suma=suma+i
    if suma==a:
        return True
    else:
        return False