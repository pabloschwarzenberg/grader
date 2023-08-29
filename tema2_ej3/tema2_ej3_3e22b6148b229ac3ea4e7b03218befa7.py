def numero_perfecto(z):
    div = []
    for j in range(1, z):
        if z%j == 0:
            i = div.append(j)
    total = 0
    for divisor in div:
        total = total + divisor
    if total == z:
        esPerfecto = True
    else:
        esPerfecto = False
    return esPerfecto