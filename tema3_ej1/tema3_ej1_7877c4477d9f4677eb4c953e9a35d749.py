def suma_divisores(n):
    dividers = []
    for i in range(1, n):
        if n%i==0:
            i = dividers.append(i)
    suma = 0
    for divider in dividers:
        suma = suma+divider
    if suma==1:
        prime = True
        return suma, prime
    else:
        prime = False
        return suma, prime