# completa el código de la función
def suma_divisores(a):
    sum = 0
    divisor = a
    while divisor > 1:
        divisor = divisor - 1
        if (a % divisor) == 0:
            sum += divisor
    return (sum, True == sum)

if __name__ == "__main__":
    print(suma_divisores(1))