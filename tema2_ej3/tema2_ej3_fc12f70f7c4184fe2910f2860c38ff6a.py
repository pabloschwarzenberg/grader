def numero_perfecto(a):
    contador=[]
    suma=0
    for i in range(1,a-1):
        if a%i==0:
            contador.append(i)
    for o in contador:
        suma=suma+o
    if suma==a:
        return True
    else:
        return False
           