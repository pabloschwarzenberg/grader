def numero_perfecto(a):
    b = 0

    for i in range(1, a):
        if a % i == 0:
            b += i
    return b == a