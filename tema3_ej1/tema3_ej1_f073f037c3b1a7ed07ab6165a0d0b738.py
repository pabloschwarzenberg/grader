# completa el código de la función
def suma_divisores(a):
    sumx = 0
    divisor = a
    while divisor > 1:
        divisor = divisor - 1
        if (a % divisor) == 0:
            sumx += divisor
    if(sumx == 1):
        return (sumx, True)
    else:
        return (sumx, False)
           