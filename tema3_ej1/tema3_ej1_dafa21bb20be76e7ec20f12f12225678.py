# completa el código de la función
def suma_divisores(q):
    sum = 0
    divisor = q
    while divisor > 1:
        divisor = divisor - 1
        if (q % divisor) == 0:
            sum += divisor
    return (sum, True == sum)

if __name__== "main":
    print(suma_divisores(1))
