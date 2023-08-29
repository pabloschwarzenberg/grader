# completa el código de la función
def suma_divisores(a):
    divisores = []
    for i in range(1,a):
        if a%i ==0:
            i = divisores.append(i)

    #sumar divisores
    suma = 0
    for divisor in divisores:
        suma+=divisor
    if suma ==1:
        esPrimo=True
        return suma, esPrimo
    else:
        esPrimo=False
        return suma, esPrimo