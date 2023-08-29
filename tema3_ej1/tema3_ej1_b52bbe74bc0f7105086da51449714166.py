# completa el código de la función
def suma_divisores(a):
    i=0
    suma=0
    while i<=a:
        k=0
        i=i+1
        if a%i==0 and i<a:
            suma=suma+i
        if suma==1:
            k=True
        if suma!=1:
            k=False
    return suma, k