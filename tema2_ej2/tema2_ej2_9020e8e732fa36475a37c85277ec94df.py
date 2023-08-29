def amigos(a, b):
    suma_divisores_a = sum([num for num in range(1, a) if a % num == 0])
    suma_divisores_b = sum([num for num in range(1, b) if b % num == 0])
    
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False