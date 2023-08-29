#Factores Primos
def descomponer_en_factores_primos(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            print(i)
    if n > 1:
        print(n)

descomponer_en_factores_primos(int(input()))