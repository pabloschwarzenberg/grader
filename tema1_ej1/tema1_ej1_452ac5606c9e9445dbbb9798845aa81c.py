#Suma de los N primeros números
#Obtener el valor de N del usuario
N = int(input("Ingrese el valor de N: "))

# Calcular la suma de los N primeros números naturales
suma = N * (N + 1) // 2

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", suma)