def suma_divisores(a):
    k=a
    suma=0
    for i in range (a-1):
        if a==1:
            suma=1
        elif a%k==0:
            suma+=a//k
        k=k-1
    if suma==1 and a!=1:
        return suma, True
    else:
        return suma, False