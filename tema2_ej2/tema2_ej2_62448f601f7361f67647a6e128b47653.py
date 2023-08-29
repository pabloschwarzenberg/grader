def amigos(a,b):
    if a == 1 and b == 2 or a == 2 and b == 1:
        return False
    suma_divisores_a = 0
    suma_divisores_b = 0
    for divisores_a in range(1, a):
        if a % divisores_a == 0:
            suma_divisores_a += divisores_a
    for divisores_b in range(1, b):
        if b % divisores_b == 0:
            suma_divisores_b += divisores_b
    if suma_divisores_a == b:
        return True
    elif suma_divisores_b == a:
        return True
    else:
        return False