def suma_divisores(n):
    div = []
    for i in range(1, n):
        if n%i == 0:
            i = div.append(i)
    
    ##sumar divisores
    suma = 0
    for divisor in div:
        suma = suma + divisor
    if suma == 1:
        Esprimo = True
        return suma, Esprimo
    else:
        Esprimo = False
        return suma, Esprimo