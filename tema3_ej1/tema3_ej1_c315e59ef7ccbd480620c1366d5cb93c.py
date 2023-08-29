def suma_divisores(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)

    ##sumar divisores
    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == 1:
        esprimo = True
        return suma, esprimo
    else:
        esprimo = False
        return suma, esprimo