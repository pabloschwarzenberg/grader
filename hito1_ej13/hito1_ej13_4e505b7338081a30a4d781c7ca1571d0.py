#Factores Primos
def descomposicion_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero // factor
        else:
            factor += 1

# Solicitar al usuario el número para descomponer
numero = int(input())

# Imprimir la descomposición de factores primos
descomposicion_factores_primos(numero)
      