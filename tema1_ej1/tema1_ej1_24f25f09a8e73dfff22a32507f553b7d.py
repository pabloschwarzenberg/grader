#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar al usuario ingresar el valor de N
n = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
suma_total = suma_numeros_naturales(n)

# Mostrar el resultado
print("La suma de los primeros", n, "números naturales es:", suma_total)