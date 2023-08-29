def suma_divisores(a):
    total = 0
    for i in range(1, a):
        if a%i == 0:
            total += i
    if total == 1:
        return total, True
    else:
        return total, False
