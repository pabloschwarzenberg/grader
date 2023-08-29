# completa el código de la función
def suma_divisores(x):
    divisor=2
    suma=1
    primo=False
    if x==1:
        return 0, primo
    while divisor<x:
        if x%divisor==0:
            suma=divisor+suma
        divisor=divisor+1
    if suma==1:
        return suma, not primo
    else:
        return suma, primo
print(suma_divisores(12))
     

           