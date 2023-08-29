#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma

n = int(input("Ingrese un numero entero positivo: "))

if n <= 0:
    print("El numero debe ser positivo.")
else:
    resultado = suma_n_primeros_numeros(n)
    print("La suma de los primeros", n, "números naturales es:", resultado)     