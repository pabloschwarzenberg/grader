# por favor escribe aquí tu función


num = int(input("Ingrese numero: "))
primos = []
for i in range(2, num + 1):
    while num % i == 0:
        primos.append(i)
        num = num / i

for i in range(len(primos)):
    print(primos[i])