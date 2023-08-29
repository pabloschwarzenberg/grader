#Suma de los N primeros números

def suma_numeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma

N = int(input("Ingrese un número entero positivo (N): "))

suma_total = suma_numeros_naturales(N)

print(suma_total)