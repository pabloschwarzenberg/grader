# completa el código de la función
def suma_divisores(a):
    divisor=1
    suma=0
    while divisor<a:
        if a%divisor==0:
            suma=suma+divisor
        divisor=divisor+1
    if suma==1:
        return suma,True
    else:
        return suma,False

       
