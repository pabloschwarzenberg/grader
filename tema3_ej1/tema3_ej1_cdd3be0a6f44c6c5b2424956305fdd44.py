def suma_divisores(a):
    divds = 0
    var = True
    if a == 1:
        return 0, False
    for n in range(1,a):
        if a%n == 0:
            divds += n
            if divds != 1:
                var = False
    return divds, var