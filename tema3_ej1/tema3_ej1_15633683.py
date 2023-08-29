def suma_divisores(a):
    suma=1
    if a==1:
        suma=0
        return suma,False
    else:
        for i in range (2,a):
            while a%i==0:
                a/=i
                suma+=i
        if suma==1:
            return suma,True
        else:
            return suma,False