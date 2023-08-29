#Suma de los N primeros números
def SumaNumeros(n):
    suma = (n * (n + 1)) // 2
    return suma

numero = int(input(">> Ingrese un número: "))

resultado = SumaNumeros(numero)

print("La suma de los", numero, "primeros números naturales es:", resultado)
