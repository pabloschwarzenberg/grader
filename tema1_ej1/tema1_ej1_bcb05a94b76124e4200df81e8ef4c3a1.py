#Suma de los N primeros números
 def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma


num = int(input("Ingresa un número entero positivo: "))

if num < 0:
    print("El número ingresado no es válido.")
else:
    resultado = suma_naturales(num)
    print("La suma de los primeros", num, "números naturales es:", resultado)     