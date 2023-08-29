# completa el código de la función
def suma_divisores(a):
    divisores = 1
    divisor = 2
    while divisor <= a:
        if a % divisor == 0:
            divisores += divisor
        divisor += 1

    divisores -= a

    if divisores == 1:
        return divisores,True
    elif divisores != 1:
        return divisores,False
           