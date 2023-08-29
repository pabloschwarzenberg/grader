def suma_divisores(n):
    divisores=[]
    numero=1
    for i in range(n-1):
        if n%numero==0:
            n=n//numero
            divisores.append(numero)
            numero=numero+1
        else:
            numero=numero+1
    suma=0
    for i in divisores:
        suma+=i
    if suma==1:
        return suma, True
    else:
        
        return suma,False