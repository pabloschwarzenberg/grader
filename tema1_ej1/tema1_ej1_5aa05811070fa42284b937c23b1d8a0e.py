#Suma de los N primeros números
def suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

numero = int(input("Ingrese un número: "))

resultado = suma_naturales(numero)
print("La suma de los", numero, "primeros números naturales es:", resultado)