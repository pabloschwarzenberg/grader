def factor_primo(num):
    factores_primos = []
    while num > 1:
        for i in range(2, int(num) + 1):
            if num % i == 0:
                factores_primos.append(i)
                num = num / i
                break
    for factor in factores_primos:
        print(factor)

numero = int(input())

factor_primo(numero)