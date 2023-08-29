#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma
numero_n = int(input("Ingrese el número N: "))
resultado = suma_n_primeros_numeros(numero_n)
print("La suma de los", numero_n, "primeros números naturales es:", resultado)      