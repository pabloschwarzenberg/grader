#Factores Primos
primos = []
n = int(input("ingrese un numero:"))
for i in range(2, n+1):
    while n%i == 0:
        x = primos.append(i)
        n = n / i

for elemento in primos:
    print(elemento)
     