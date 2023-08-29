#Factores Primos
def descomposicion_factores_primos(numero):
    factor = 2
    while factor * factor <= numero:
        if numero % factor:
            factor += 1
        else:
            numero //= factor
            print(factor)
    if numero > 1:
        print(numero)

numero = int(input())
descomposicion_factores_primos(numero)
      