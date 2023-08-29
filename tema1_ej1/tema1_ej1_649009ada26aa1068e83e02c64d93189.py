#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número entero positivo: "))

# Verificar si el número ingresado pertenece a los naturales 
if numero <= 0:
    print("El número debe ser entero mayor o igual que cero.")
else:
    resultado = suma_numeros_naturales(numero)
    print("La suma de los primeros", numero, "números naturales es:", resultado)