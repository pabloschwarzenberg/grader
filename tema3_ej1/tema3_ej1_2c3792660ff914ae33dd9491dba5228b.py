# completa el código de la función
def suma_divisores(a):
    divisores=1
    suma=0
    while divisores<a:
        if a%divisores==0:
            suma=suma+divisores
        divisores=divisores+1
    if suma!=1:
        return (suma, False)
    else:
        return (suma, True)
 