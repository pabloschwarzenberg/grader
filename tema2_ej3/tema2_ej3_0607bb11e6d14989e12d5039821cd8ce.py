def numero_perfecto(a):
    suma=0
    NActual=1
    if a==1:
     return 0,False
    else:
     while NActual != a:
        if a%NActual==0:
            suma=suma+NActual
        NActual=NActual+1
    if suma==a:
        return True
    else:
     return False
           