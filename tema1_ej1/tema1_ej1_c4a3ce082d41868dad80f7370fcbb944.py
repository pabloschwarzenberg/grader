#Suma de los N primeros números
n = int(input("Ingresa un número entero positivo: "))

if n < 0:
    print("El número ingresado no es válido.")
else:
    suma = n * (n + 1) // 2
    print("La suma de los " + str(n) + " primeros números naturales es: " + str(suma))
