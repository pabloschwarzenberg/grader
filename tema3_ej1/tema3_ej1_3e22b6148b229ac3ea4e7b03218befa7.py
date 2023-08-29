def suma_divisores(n):
    div = []
    for i in range(1, n):
        if n%i == 0:
            i = div.append(i)
    sum = 0
    for divisor in div:
        sum = sum + divisor
    if sum == 1:
        esPrimo = True
        return sum, esPrimo
    else:
        esPrimo = False
        return sum, esPrimo