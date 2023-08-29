#Factores Primos
def factorizar(num):
    for i in range(2, num // 2 + 1):
        while num % i == 0:
            print(i)
            num //= i

    if num > 1:
        print(num)


numero = int(input())
factorizar(numero)     