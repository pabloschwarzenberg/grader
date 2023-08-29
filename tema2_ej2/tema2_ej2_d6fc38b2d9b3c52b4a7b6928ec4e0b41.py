def amigos(a, b):
    if a == b:
        return False
    suma_a = sum([i for i in range(1, a) if a % i == 0])
    suma_b = sum([i for i in range(1, b) if b % i == 0])
    if suma_a == b and suma_b == a:
        return True
    else:
        return False