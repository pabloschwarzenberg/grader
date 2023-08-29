def numero_perfecto(a):
    suma_de_divisores = 0
    for i in range(1, a):
        if a % i == 0:
            suma_de_divisores += i
    if suma_de_divisores == a:
        return True
    else:
        return False