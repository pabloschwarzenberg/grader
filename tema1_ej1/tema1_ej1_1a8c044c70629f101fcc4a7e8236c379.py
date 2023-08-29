#Inicio
#Suma de los N primeros números
#Ingreso de variables
N = int(input("Ingrese un número entero positivo: "))

#Verificar si N es un número entero positivo
if N <= 0:
    print("El número ingresado debe ser un entero positivo.")
else:
#Calcular la suma de los N primeros números naturales
    suma = sum(range(1, N + 1))

#Imprimir la suma
    print("La suma de los primeros", N, "números naturales es:", suma)
#Fin

