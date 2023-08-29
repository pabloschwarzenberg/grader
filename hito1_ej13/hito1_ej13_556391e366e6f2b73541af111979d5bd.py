#Factores Primos
numero = int(input())

def descomposicion_factores_primos(numero):
    factor = 2
    while factor * factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero //= factor
        else:
            factor += 1
    if numero > 1:
        print(numero)

descomposicion_factores_primos(numero)
      