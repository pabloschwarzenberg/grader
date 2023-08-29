#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Pedir al usuario que ingrese el número N
numero_N = int(input("Ingresa el número N: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_n_primeros_numeros(numero_N)

# Mostrar el resultado
print("La suma de los", numero_N, "primeros números naturales es:", resultado)

     