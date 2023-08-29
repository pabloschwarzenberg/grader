
def suma_divisores(a):
    contador=0
    suma=0
    for divisor in range(1,a+1):
        if (a%divisor)==0:
            if divisor != a:
                suma=suma+divisor
            contador=contador+1
    if suma==1:
        return ("el numero "+str(a)+" es primo")
    else:
        return ("el numero "+str(a)+" no es primo")