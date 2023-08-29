def numero_perfecto(a):
    c=1
    suma=0
    while c!=a:
        if a%c==0:
            suma=suma+c
        c=c+1
    if suma==a:
        return True
    else:
        return False
         