#Factores Primos
def descomposicion_factores_primos(numero):
    
    factores_primos = []

    
    for i in range(2, numero // 2 + 1):
        
        while numero % i == 0:
            factores_primos.append(i)
            numero //= i

    
    if numero > 1:
        factores_primos.append(numero)

    
    for factor in factores_primos:
        print(factor)


numero = int(input())


descomposicion_factores_primos(numero)     