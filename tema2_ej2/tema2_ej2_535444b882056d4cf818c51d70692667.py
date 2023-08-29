def son_amigos(a, b):
    suma_divisores_a = sum([i for i in range(1, a) if a % i == 0])
    suma_divisores_b = sum([i for i in range(1, b) if b % i == 0])

    return suma_divisores_a == b and suma_divisores_b == a

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if son_amigos(a, b):
    print(f"{a} y {b} son números amigos")
else:
    print(f"{a} y {b} no son números amigos") 