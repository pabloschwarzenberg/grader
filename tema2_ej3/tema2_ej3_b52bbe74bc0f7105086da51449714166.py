def numero_perfecto(a):
    i=0
    suma=0
    while i<=a:
        i=i+1
        if a%i==0 and i<a:
            suma=suma+i
    if suma==a:
        return True
    else:
        return False
           