def amigos(x, y):
    suma = 0
    suma1 = 0
    for i in range(1, x):
        if x % i == 0:
            suma += i

    for k in range(1, y):
        if y % k == 0:
            suma1 += k

    if (x == suma1) and (y == suma):
        return True
    else:
        return False
