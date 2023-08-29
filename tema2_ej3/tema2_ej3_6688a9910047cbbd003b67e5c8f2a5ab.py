def numero_perfecto(n):
    i=1
    divisores=[]
    while i<n:
        if n%i==0:
            divisores.append(i)
            i=i+1
        else:
            i=i+1
    suma=0
    for l in divisores:
        suma=suma + l
    if suma==n:
        return True
    else:
        return False
           