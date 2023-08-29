def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma
n = int(input("Ingresa un número N: "))
resultado = suma_naturales(n)
print({resultado})