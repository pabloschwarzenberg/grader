# completa el código de la función
def suma_divisores(a):
    sum = 0
    div = a
    while div > 1:
        div = div - 1
        if (a % div) == 0:
            sum += div
    if a<2:
        return sum, False
    for i in range(2, a):
        if a %i==0:
            return sum, False
    return sum, True
           