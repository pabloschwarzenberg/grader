def esPrimo(a):
    suma = 0
    primo = True
    for divisor in range(1, a):
        if a % divisor == 0:
            suma += divisor
    if suma != 1:
        primo = False
    return primo


def descomposicionPrimos(n):
    primos = []
    for numero in range(2, n + 1):
        if esPrimo(numero):
            primos.append(numero)

    for primo in primos:
        if n % primo == 0:
            n = n / primo
            print(primo)


n = int(input())
descomposicionPrimos(n)