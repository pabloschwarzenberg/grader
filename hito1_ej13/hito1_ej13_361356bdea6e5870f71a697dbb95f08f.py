n = int(input('Ingresa un numero entero: '))

for i in range(2, n+1):
    while n % i == 0:
        print(i)
        n = n / i