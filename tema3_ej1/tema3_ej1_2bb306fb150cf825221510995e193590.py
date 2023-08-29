# completa el código de la función
def suma_divisores(x):
    sum = 0
    divisor = x
    while divisor > 1:
        divisor = divisor - 1
        if (x % divisor) == 0:
            sum += divisor
    return (sum, True == sum)

if __name__== "main":
    print(suma_divisores(1))