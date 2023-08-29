a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

divisores_a = []
for i in range(1, a):
    if a % i == 0:
        divisores_a.append(i)

divisores_b = []
for i in range(1, b):
    if b % i == 0:
        divisores_b.append(i)

suma_divisores_a = sum(divisores_a)
suma_divisores_b = sum(divisores_b)

if suma_divisores_a == b and suma_divisores_b == a:
    print("Son números amigos")
else:
    print("No son números amigos")
