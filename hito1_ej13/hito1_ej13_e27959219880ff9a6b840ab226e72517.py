#Factores Primos
def descomposicion_factores_primos(numero):
    # Inicializar lista de factores primos
    factores_primos = []

    # Obtener los factores primos del número
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            factores_primos.append(divisor)
            numero = numero / divisor
        else:
            divisor += 1

    return factores_primos

# Solicitar al usuario el número a descomponer
numero = int(input())

# Obtener los factores primos del número
factores_primos = descomposicion_factores_primos(numero)

# Imprimir cada factor primo en una línea separada
for factor in factores_primos:
    print(factor)
      