def numero_perfecto(a):
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
    if suma==a:
        return True
    else:
        return False
        return suma    
           