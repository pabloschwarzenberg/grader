def suma_divisores(numero):
    divisor=1
    d=0
    suma=0
    cantidad_divisores=0
    while divisor<numero:
        d=numero%divisor
        if d==0:
            suma=suma+divisor
            cantidad_divisores=cantidad_divisores+1
        divisor=divisor+1
    if(cantidad_divisores==1):
        return suma,True
    else:
        return suma,False


