#Factores Primos
def descomposicion_factores_primos(n):
    factor = 2

    while factor <= n:
        if n % factor == 0:
            print(factor)
            n = n // factor
        else:
            factor += 1

n = int(input("Ingrese numero: "))
descomposicion_factores_primos(n)        