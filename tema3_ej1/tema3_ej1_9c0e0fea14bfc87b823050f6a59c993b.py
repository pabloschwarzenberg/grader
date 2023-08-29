def suma_divisores(a):
    suma_div = 0
    division = a
    while division > 1:
        division = division - 1
        if (a% division) == 0:
            suma_div += division
    if (suma_div == 1):
        return suma_div, True
    else:
        return suma_div, False