def suma_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

N = int(input())

resultado = suma_naturales(N)

print(resultado)
