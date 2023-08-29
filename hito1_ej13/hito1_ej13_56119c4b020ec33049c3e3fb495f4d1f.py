#Factores Primos
def descomponer_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero // factor
        else:
            factor += 1

num = int(input())
descomponer_factores_primos(num)
