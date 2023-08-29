#Suma de los N primeros números
def calcular_suma_primeros_n_numeros(n):
    suma = n * (n + 1) // 2
    return suma


# Solicitar al usuario un número N
numero = int(input("Ingrese un número N: "))

# Calcular la suma de los primeros N números naturales
suma_total = calcular_suma_primeros_n_numeros(numero)

# Imprimir el resultado
print("La suma de los primeros", numero, "números naturales es:", suma_total)