#Factores Primos
numero = int(input())

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def descomposicion_factores_primos(num):
    for i in range(2, num + 1):
        if num % i == 0 and es_primo(i):
            print(i)

descomposicion_factores_primos(numero)
      