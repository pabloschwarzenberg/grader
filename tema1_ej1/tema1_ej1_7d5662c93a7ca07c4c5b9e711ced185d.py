#Suma de los N primeros números
# Solicitar al usuario que ingrese un número N
N = int(input("Ingrese un número: "))

# Calcular la suma de los N primeros números naturales
suma = N * (N + 1) // 2

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", suma)      