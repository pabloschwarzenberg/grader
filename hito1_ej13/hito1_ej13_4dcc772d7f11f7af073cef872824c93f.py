#Factores Primos
n = int(input("ingrese numero: "))

primos= []

for i in range (2, n+1):
    while n % i == 0:
        primos.append(i)
        n = n / i
print(primos)