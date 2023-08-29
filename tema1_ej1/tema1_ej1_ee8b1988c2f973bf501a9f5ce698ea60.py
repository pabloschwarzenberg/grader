def suma_numeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar el número al usuario
N = int(input("Ingrese un número entero: "))

# Calcular la suma de los primeros N números naturales
suma_total = suma_numeros_naturales(N)

# Imprimir la suma
print("La suma de los primeros", N, "números naturales es:", suma_total)

      