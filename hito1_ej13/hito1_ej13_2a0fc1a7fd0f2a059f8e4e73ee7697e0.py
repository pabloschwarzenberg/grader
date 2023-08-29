#Factores Primos
def factores_primos(numero):
    i = 2
    while i <= numero:
        if numero % i == 0:
            print(i)
            numero = numero / i
        else:
            i += 1

numero = int(input())
factores_primos(numero)
     