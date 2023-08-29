# Ingresar el número N
while True:
    try:
        N = int(input("Ingrese un número N: "))
        break
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

# Calcular la suma de los N primeros números naturales
suma = N * (N + 1) // 2

# Imprimir la suma
print("La suma de los", N, "primeros números naturales es:", suma)

#FIN