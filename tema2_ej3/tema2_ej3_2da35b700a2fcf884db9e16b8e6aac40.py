def numero_perfecto(a):
    indice = a
    suma_divisores = 0
    while indice > 0:
        if a != indice:
            if a % indice == 0:
                suma_divisores += indice
        indice -= 1
    if suma_divisores == a:
        return True
    return False