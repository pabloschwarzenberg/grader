#Factores Primos
x = int(input("ingrese el numero:"))

primos = []

for i in range(2, x+1):
    while x % i == 0:
        primos.append(i)
        x = x / i
print(primos)
     