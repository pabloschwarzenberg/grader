# completa el código de la función
def suma_divisores (numero):
    suma=0
    divisor=numero
    if numero==1:
        return 0, False
    while divisor > 1:
        divisor+=-1
        if numero%divisor==0:
            suma+=divisor
        if divisor==1:
            if suma==1:
                return suma,True
            if suma>1:
                return suma,False