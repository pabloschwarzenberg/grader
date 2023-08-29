# completa el código de la función
def suma_divisores(a):
    sumaDeDivisores = 0
    esPrimo = False
    for numero in range(1,a):
        modulo = a % numero
        if (modulo == 0):
            sumaDeDivisores = sumaDeDivisores + numero

    if (sumaDeDivisores == 1):
        esPrimo = True
    else:
        esPrimo = False
    return sumaDeDivisores, esPrimo