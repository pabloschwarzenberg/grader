#Suma de los N primeros números
def suma_n_primeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma
    
N = int(input("Ingrese un número entero positivo: "))

resultado = suma_n_primeros_naturales(N)
print("La suma de los primeros", N, "números naturales es:", resultado)