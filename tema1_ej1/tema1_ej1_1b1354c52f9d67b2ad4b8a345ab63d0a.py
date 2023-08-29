#Suma de los N primeros números
def suma_n_primeros_numeros(N):
    suma = N * (N + 1) // 2
    return suma
N = int(input("Ingrese el valor de N: "))
resultado = suma_n_primeros_numeros(N)
print("La suma de los", N, "primeros números naturales es:", resultado)