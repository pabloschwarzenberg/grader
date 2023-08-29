def suma_divisores(n):
    s = 0
    d = n
    while d > 1:
        d = d - 1
        if (n % d) == 0:
            s += d
    if n<2:
        return s, False
    for i in range(2, n):
        if n %i==0:
            return s, False
    return s, True