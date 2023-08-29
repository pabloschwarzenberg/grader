#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma


N = int(input("Ingrese un número entero positivo: "))


if N <= 0:
    print("El número debe ser positivo.")
else:
   
    suma_total = suma_numeros_naturales(N)

    
    print("La suma de los", N, "primeros números naturales es:", suma_total)