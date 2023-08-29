#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2 
    print("La suma de los", n, "primeros números naturales es:", suma)
N = int(input("Ingrese un número entero positivo: "))
if N < 0:
    print("El número ingresado no es válido. Debe ser un número entero positivo.")
else:

    suma_n_primeros_numeros(N)

      