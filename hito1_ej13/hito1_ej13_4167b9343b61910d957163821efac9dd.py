#Factores Primos
def factor_primo(numero):
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            print(divisor)
            numero = numero // divisor
        else:
            divisor += 1

numero = int(input())

factor_primo(numero)
