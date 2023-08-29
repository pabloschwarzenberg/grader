def amigos(a, b):
    divisores_a = 0
    divisores_b = 0
    for i in range(1, a):
        if a % i == 0:
            divisores_a = divisores_a + i
    for i in range(1, b):
        if b % i == 0:
            divisores_b = divisores_b + i
    if divisores_a == b and divisores_b == a:
        return True
    else:
        return False