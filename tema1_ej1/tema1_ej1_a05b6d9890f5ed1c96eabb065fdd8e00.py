#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar al usuario que ingrese el número N
numero = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los primeros N números
suma_total = suma_n_primeros_numeros(numero)

# Imprimir la suma
print("La suma de los primeros", numero, "números naturales es:", suma_total)
      