#Factores Primos
def descomposicion_factores_primos(numero):
    divisor = 2

    while numero > 1:
        while numero % divisor == 0:
            print(divisor)
            numero //= divisor
        divisor += 1

numero = int(input())

descomposicion_factores_primos(numero)     