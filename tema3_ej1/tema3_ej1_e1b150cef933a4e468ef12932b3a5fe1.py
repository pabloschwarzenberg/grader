def suma_divisores(p):
    sumar = 0
    for a in range(1,p):
        if p % a == 0:
            sumar = sumar + a

    y = True
    if p <= 1:
        y = False
    elif p == 2:
        y = True
    else:
        for a in range(2, p):
            if p % a == 0:
                y = False

    return (sumar,y)