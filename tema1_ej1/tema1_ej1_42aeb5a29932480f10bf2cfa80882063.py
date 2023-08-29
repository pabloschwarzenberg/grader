#Suma de los N primeros números
def suma_n_primeros_naturales(n):
    suma = n * (n + 1) // 2
    print("La suma de los", n, "primeros números naturales es:", suma)

# Solicitar el valor de N al usuario
N = int(input("Ingrese el valor de N: "))

# Llamar a la función para calcular la suma
suma_n_primeros_naturales(N)
