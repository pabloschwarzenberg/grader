def numero_perfecto(n):
    dividers = []
    for i in range(1, n):
        if n%i == 0:
            i = dividers.append(i)

    partial = 0
    for divider in dividers:
        partial += divider
    if partial == n:
        isPerfect = True
    else:
        isPerfect = False
    return isPerfect