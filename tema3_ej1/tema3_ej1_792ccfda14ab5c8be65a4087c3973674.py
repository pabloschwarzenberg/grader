def suma_divisores(a):
    x = 0
    i = 1
    while i < a:
        if a % i == 0:
            x = x + i
        i = i +1

    for i in range(2,a):
        if a%i == 0:
            return x, False
    if a%i != 0 and a >1:
        return x, True
    return x, False