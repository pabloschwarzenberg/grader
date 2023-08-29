def numero_perfecto(a):
    suma = 0

    for i in range(1, a):
        if a % i == 0:
            suma += i
    return suma == a

print(numero_perfecto(6))
print(numero_perfecto(12))