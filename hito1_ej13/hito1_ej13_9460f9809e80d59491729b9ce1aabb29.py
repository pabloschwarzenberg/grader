#Factores Primos
def factorizar(numero):
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            print(divisor)
            numero = numero / divisor
        else:
            divisor += 1

numero = int(input())

factorizar(numero)
      