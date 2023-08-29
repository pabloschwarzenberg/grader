#Factores Primos
def des(n):
    primos = []
    for i in range(2, n + 1):
        while n % i == 0:
            primos.append(i)
            n = n / i
    return primos
x = des(int(input("Ingrese el numero: ")))
for i in x:
    print(i)
 