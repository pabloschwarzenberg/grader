def amigos(a, b):
    suma_a = 0
    suma_b = 0

    for i in range(1, a):
        if a % i == 0:
            suma_a += i

    for j in range(1, b):
        if b % j == 0:
            suma_b += j

    if suma_a == b and suma_b == a:
        return True
    else:
        return False
