def suma_divisores(a):
    divisores = []
    for j in range(1, a):
        if ((a % j) == 0):
            j = divisores.append(j)
    total = 0
    for d in divisores:
        total = (total + d)
    if (total == 1):
        p = True
        return total, p
    else:
        p = False
        return total, p