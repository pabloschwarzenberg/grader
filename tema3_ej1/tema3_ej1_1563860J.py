# completa el código de la función
def suma_divisores(a):
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
    if suma!=1:
        return suma, False
    elif suma==1:
        return 1, True
    elif suma==0:
        return 0,False
