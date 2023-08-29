# completa el código de la función
def suma_divisores(a):
    sum_div = 0
    i = 0
    for i in range(1,a):
        if (a % i) == 0:
            sum_div += i
            i += 1
    if sum_div == 1:
        return sum_div, True
    else:
        return sum_div, False