def factor_primo(numero):
    i = 2
    while i <= numero:
        if numero % i == 0:
            print(i)
            numero = numero / i
        else:
            i += 1

numero = int(input())

print("Descomposición de factores primos:")
factor_primo(numero)

      