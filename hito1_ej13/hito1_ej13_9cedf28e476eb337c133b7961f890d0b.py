#Factores Primos
n = int(input('ingrese el numero: '))
primos = []
for i in range(2, n + 1):
    while n % i == 0:
        primos.append(i)
        n = n / i
for n in primos:
    print(n)