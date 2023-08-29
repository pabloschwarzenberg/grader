#Suma de los N primeros números
def suma_naturales(n):
    suma = n * (n + 1) // 2
    return suma


Naturales = int(input("Ingrese un número N: "))


sumastotal = suma_naturales(Naturales)


print("La suma de los", Naturales, "primeros números naturales es:", sumastotal)