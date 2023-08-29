def numero_perfecto(n):
    d = 1
    suma_divisores = 0
    while d < n:
        if n%d == 0:
            suma_divisores += d
            d += 1

        else:
            d += 1
    if suma_divisores == n:
        return True
    else:
        return False