def descomposicion_factores_primos(numero):
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    factores_primos = []
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            if es_primo(divisor):
                factores_primos.append(divisor)
                numero //= divisor
            else:
                divisor += 1
        else:
            divisor += 1

    for factor in factores_primos:
        print(factor)

numero = int(input())

descomposicion_factores_primos(numero)