#Suma de los N primeros números
def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma

n = int(input("Ingrese un número: "))

# Verificar si el número ingresado es positivo
if n < 0:
    print("El número ingresado debe ser positivo.")
else:
    r = suma_naturales(n)
    print(f"La suma de los {n} primeros números naturales es: {r}")
