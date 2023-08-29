def factor_primo(n):
    factores_primos = []

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factores_primos.append(i)
            n //= i
            
    if n > 1:
        factores_primos.append(n)
        
    for factor in factores_primos:
        print(factor)

numero = int(input())
factor_primo(numero)