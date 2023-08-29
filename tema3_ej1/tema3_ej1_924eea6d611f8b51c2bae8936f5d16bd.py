# completa el código de la función
def suma_divisores(a):
    sum = 0
    divisor = a
    while divisor > 1:
        divisor = divisor - 1
        if (a % divisor) == 0:
            sum += divisor
    if a<2:
        return sum, False
    for i in range(2, a):
        if a %i==0:
            return sum, False
    return sum, True           