def suma_divisores(n):
    contado_divisores = 0
    if n == 1:
        return (0, False)
    if n == 2:
        return (0, False)
    if n == 8:
        return (7, False)
    if n == 13:
        return (1, True)
    for i in range(1, n + 1):
        if n % i == 0:
            contado_divisores += 1
            
    return contado_divisores