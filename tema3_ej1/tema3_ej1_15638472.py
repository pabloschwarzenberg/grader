# completa el código de la función
def suma_divisores(a):
    suma=1
    p=2
    while p!=a and a!=1:
        if a%p==0:
            suma=suma+p
            p=p+1
        else:
            p=p+1
    if a==1:
        suma=0
    if suma==1:
        y=True
    else:
        y=False
    return suma,y
           