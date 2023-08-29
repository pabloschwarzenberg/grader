def numero_perfecto(a):
    c=1
    suma_a=0
    while (c<a):
        if a%c==0:
            suma_a=suma_a+c
        c=c+1
    if(suma_a==a):
        return True
    else:
        return False