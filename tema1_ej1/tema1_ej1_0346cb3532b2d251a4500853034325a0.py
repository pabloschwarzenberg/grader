#Suma de los N primeros números
print("Ingrese un número entero positivo: ")
n = int(input(">>>"))

if n <= 0:
    print("El número ingresado no es válido.")
else:
    suma = n * (n + 1) // 2

    print("La suma de los", n, "primeros números naturales es:", suma)      