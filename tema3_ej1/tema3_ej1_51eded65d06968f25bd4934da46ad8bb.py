def suma_divisores(suma_divisores):
    suma = 0
    for i in range(1, suma_divisores):
        if suma_divisores % i == 0:
            suma += i
    return suma


suma_divisores=int(input("Ingresa el número: "))
print("La suma es de sus divisores es: ")
print(suma_divisores(suma_divisores))