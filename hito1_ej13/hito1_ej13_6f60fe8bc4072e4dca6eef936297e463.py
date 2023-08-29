def descomponer_en_factores_primos(n):
    factor = 2
    while n > 1:
        if n % factor == 0:
            print(factor)
            n = n // factor
        else:
            factor += 1

n = int(input("Ingrese un número: "))
descomponer_en_factores_primos(n)
