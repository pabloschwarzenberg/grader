#Suma de los N primeros números
# Solicitar el número N al usuario
N = int(input("Ingrese el número N: "))

# Calcular la suma de los N primeros números naturales utilizando la fórmula
suma = N * (N + 1) // 2

# Mostrar el resultado
print("La suma de los", N, "primeros números naturales es:", suma)
