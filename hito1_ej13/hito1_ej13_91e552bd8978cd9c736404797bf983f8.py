#Factores Primos
def factor_primo(numero):
    factor = 2

    while factor * factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero //= factor
        else:
            factor += 1

    if numero > 1:
        print(numero)

numero = int(input())

factor_primo(numero)
