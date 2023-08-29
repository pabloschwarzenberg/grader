#Suma de los N primeros números
 # Obtener el número N del usuario
N = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los primeros N números naturales
suma = N * (N + 1) // 2

# Imprimir la suma de los N primeros números naturales
print("La suma de los primeros", N, "números naturales es:", suma)
