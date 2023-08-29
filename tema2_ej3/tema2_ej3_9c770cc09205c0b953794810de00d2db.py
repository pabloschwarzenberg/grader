def numero_perfecto(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)

    ##sumar divisores
    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == n:
        esPerfecto = True
    else:
        esPerfecto = False
    return esPerfecto