def suma_divisores(n):
    D_I = []
    for i in range(1, n):
        if n%i == 0:
            i = D_I.append(i)

    suma = 0
    for div in D_I:
        suma = suma + div
    if suma == 1:
        NUMPrimo = True
        return suma, NUMPrimo
    else:
        NUMPrimo = False
        return suma, NUMPrimo
           