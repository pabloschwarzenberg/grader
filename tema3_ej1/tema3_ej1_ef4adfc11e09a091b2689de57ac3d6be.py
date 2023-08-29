# completa el código de la función
def suma_divisores(a):
    n = 1
    div = 0
    while n < a:
        if a % n == 0:
            div += n
        n += 1
    if div > 1 and a != 1:
        neo_div = (div, False)
    elif a == 1:
        neo_div = (div, False)
    else:
        neo_div = (div, True)
    return neo_div
           