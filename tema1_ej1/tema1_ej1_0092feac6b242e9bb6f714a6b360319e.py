#Suma de los N primeros números
def calcular_suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
resultado = calcular_suma_naturales(numero)
print("La suma de los", numero, "primeros números naturales es:", resultado)
     