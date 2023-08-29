#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    print("La suma de los primeros", n, "números naturales es:", suma)

# Solicitar al usuario ingresar el valor de N
N = int(input("Ingrese el valor de N: "))

# Llamar a la función para calcular e imprimir la suma
suma_n_primeros_numeros(N)
      