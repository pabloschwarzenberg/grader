# completa el código de la función
def suma_divisores(a):
    suma=0
    NActual=1
    if a==1:
     return 0,False
    else:
     while NActual != a:
        if a%NActual==0:
            suma=suma+NActual
        NActual=NActual+1
    if suma==1:
        return suma,True
    else:
     return suma,False
           