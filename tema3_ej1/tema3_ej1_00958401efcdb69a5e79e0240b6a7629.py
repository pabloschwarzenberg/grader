import math

def suma_divisores(a):
    suma=0
    i=1
    while i<a:
        resultado=(a%i)
        if resultado==0:
            suma=suma+i
        i=i+1
    if suma==1:
        b=True
    else:
        b=False
    return suma,b

resultado=suma_divisores(10)
print (resultado)
           