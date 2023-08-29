def suma_divisores(a):
    numeros = 0
    for i in range(1, a):
        if a % i == 0:
            numeros = numeros + i
    if numeros == 0:
        return numeros, False
    if numeros == 1:
        return numeros, True
    if numeros > 1:
        return numeros, False
