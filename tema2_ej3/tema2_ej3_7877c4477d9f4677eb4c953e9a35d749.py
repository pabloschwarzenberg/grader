def numero_perfecto(n):
    dividers = []
    for i in range(1, n):
        if n%i==0:
            i = dividers.append(i)

    suma = 0
    for divider in dividers:
        suma = suma+divider
    if suma==n:
        perfect = True
    else:
        perfect = False
    return perfect           