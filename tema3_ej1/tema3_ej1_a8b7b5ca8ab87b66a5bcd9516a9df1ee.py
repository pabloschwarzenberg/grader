# completa el código de la función
def suma_divisores(a):
    i=1
    suma=0
    while i < a:
        if a%i==0:
            suma=i+suma
            i=i+1
        else:
            i=i+1
    if suma==1:
        primo=True
    else:
        primo=False
    return suma,primo


           