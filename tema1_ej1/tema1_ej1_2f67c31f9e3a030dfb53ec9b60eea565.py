#Suma de los N primeros números
def suma_n_numeros(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar al usuario que ingrese el número N
N = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los N primeros números naturales llamando a la función
resultado = suma_n_numeros(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)