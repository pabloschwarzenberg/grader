# completa el código de la función
def suma_divisores(a):
    i=1
    suma=0
    x=0
    while i<a:
        if a%i==0:
            suma=suma+i
        i=i+1
    if a==1:
        suma=0
        x=False
    elif suma==1:
        x=True
    else:
        x=False
    return suma,x    
a=8
suma_divisores(a)
           