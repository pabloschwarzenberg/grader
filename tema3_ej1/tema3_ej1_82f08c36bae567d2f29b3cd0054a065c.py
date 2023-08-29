# completa el código de la función
def suma_divisores(x):
    sum = 0
    div = x
    while div > 1:
        div -= 1
        if (x % div) == 0:
            sum += div
    return (sum, True == sum)