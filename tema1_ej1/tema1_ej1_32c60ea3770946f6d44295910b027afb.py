#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2  # Calcula la suma de los N primeros números naturales
    return suma

# Solicita al usuario ingresar el valor de N
N = int(input("Ingresa un número entero positivo: "))

# Verifica que el número ingresado sea válido
if N <= 0:
    print("El número ingresado debe ser positivo.")
else:
    # Calcula y muestra la suma de los N primeros números naturales
    resultado = suma_n_primeros_numeros(N)
    print("La suma de los primeros", N, "números naturales es:", resultado)
