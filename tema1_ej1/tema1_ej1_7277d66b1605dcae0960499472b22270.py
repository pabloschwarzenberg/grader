#Suma de los N primeros números
def sum_n(n):
    suma = n * (n + 1) // 2
    return suma
N = int(input("Ingrese un número: "))
resultado = sum_n(N)
print("La suma de los primeros", N, "números naturales es:", resultado)      