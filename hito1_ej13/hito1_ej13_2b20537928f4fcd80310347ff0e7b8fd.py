def factor_primo(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero / factor
        else:
            factor += 1

num = int(input())

print("La descomposición en factores primos del número", num, "es:")
factor_primo(num)
