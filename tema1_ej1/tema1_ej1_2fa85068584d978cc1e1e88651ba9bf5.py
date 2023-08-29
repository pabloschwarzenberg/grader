#Suma de los N primeros números
 # Obtener el valor de N desde el usuario
N = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
suma = N * (N + 1) // 2

print("La suma de los " + str(N) + " primeros números naturales es: " + str(suma))