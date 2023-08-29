#Suma de los N primeros números
print("Ingrese los primeros numeros naturales")
def suma_num_naturales(n):
    suma = n * (n + 1)/2
    return suma
N = int(input("Ingrese un numero N: "))

resultado = suma_num_naturales(N)

print("La suma de los", N, "primeros numeros naturales es:", resultado)

