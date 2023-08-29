# completa el código de la función
def suma_divisores(n):
    suma = 0
    divisor = n
    while divisor > 1:
        divisor = divisor - 1
        if (n % divisor) == 0:
            suma += divisor
    esPrimo=True
    if n == 1 :
        esPrimo=False
    else :
        for x in range(2, n-1):
            if n % x == 0:
                esPrimo=False
                break
    return suma, esPrimo

if __name__ == "__main__":
    print(suma_divisores(1))