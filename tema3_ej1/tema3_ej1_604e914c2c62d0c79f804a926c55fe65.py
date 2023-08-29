# completa el código de la función
def suma_divisores(a):
    divisor=1
    suma=0
    while a>divisor:
        if a%divisor==0:
            suma=suma+divisor
        divisor=divisor+1
    if suma==1:
        a=True
    else:
        a=False
    return suma,a
           