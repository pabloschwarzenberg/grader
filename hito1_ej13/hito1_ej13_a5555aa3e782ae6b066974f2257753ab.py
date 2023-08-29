#Factores Primos
def descomposicion_factores_primos(numero):
    i = 2
    while i <= numero:
        if numero % i == 0:
            print(i)
            numero = numero / i
        else:
            i = i + 1

numero = int(input())

descomposicion_factores_primos(numero)