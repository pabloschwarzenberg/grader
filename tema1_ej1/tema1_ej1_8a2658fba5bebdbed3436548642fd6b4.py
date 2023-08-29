#Colocar la funcion para la suma de n numeros naturales
def suma_n_numeros(n):
    suma = n * (n + 1) // 2
    return suma

#Pedir que N sea un numero positivo para que cumpla la siguiente variable
N = int(input("Ingresa un número entero positivo: "))

# Ya que piden numeros naturales N debe ser mayor a 0 para que se cumpla las variables
if N < 0:
    print("El número debe ser positivo.")
else:
    resultado = suma_n_numeros(N)
    print("La suma de los", N, "números naturales es:", resultado)
