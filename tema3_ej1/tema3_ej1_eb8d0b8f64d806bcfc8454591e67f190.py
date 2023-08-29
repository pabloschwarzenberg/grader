# completa el código de la función
def suma_divisores(a):
    suma_divisores=0
    for i in range (1,a):
        if a%i==0:
            suma_divisores=suma_divisores+i
    if suma_divisores==1:
        return (suma_divisores,True)
    else:
        return (suma_divisores,False)

           