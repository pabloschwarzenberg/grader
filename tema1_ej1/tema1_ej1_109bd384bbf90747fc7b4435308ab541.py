def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Solicitar al usuario ingresar el número N
numero = int(input("Ingrese un número entero: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_naturales(numero)

# Imprimir la suma
print("La suma de los", numero, "primeros números naturales es:", resultado)