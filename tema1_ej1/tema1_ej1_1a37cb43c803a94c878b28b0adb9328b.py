#Suma de los N primeros números
def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

numero = int(input("Ingrese un número N: "))
print("La suma de los primeros", numero, "números naturales es:", suma_naturales(numero))