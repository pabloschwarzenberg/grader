# completa el código de la función
def suma_divisores(a):
    suma_divisores=0
    primo=False
    for i in range(1,a):
        if a%i==0:
            suma_divisores=suma_divisores+i
    if suma_divisores==1:
        primo=True
    return suma_divisores,primo