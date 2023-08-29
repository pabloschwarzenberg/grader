#Factores Primos
def descomposicion_factores_primos(numero):
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factores_primos = []

    for i in range(2, numero + 1):
        if es_primo(i):
            while numero % i == 0:
                factores_primos.append(i)
                numero //= i

    for factor in factores_primos:
        print(factor)

numero = int(input())

descomposicion_factores_primos(numero)