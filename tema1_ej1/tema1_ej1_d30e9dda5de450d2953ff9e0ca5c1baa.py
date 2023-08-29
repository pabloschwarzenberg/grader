#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    print("La suma de los primeros", n, "números naturales es:", suma)

# Ejemplo de uso
numero = int(input("Ingrese un número entero positivo: "))

suma_n_primeros_numeros(numero)