def suma_divisores(n):
    d = 1
    suma_divisores = 0
    while d < n:
        if n%d == 0:
            suma_divisores += d
            d += 1

        else:
            d += 1
    print(suma_divisores)
    if suma_divisores == 1:
        return suma_divisores,True
    else:
        return suma_divisores,False


           