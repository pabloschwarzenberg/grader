def numero_perfecto(n):
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    if suma_divisores == n:
        return True
    else:
        return False
