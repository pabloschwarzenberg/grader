def numero_perfecto(a):
    suma_div = sum([i for i in range(1,a) if a % i == 0])
    if suma_div == a:
        return True
    return False