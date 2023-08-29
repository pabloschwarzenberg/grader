#Factores Primos
n = int(input("Ingrese un numero: "))
for i in range(2, n+1):
    while n % i == 0:
        n = n/i
        print(i)
        