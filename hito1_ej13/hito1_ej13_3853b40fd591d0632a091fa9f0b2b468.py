n = int(input("Ingrese un número: "))

divisores = []

for i in range(2, n+1):
    while n % i == 0:
        divisores.append(i)
        n = n/i

for x in range(len(divisores)):
    print(divisores[x])