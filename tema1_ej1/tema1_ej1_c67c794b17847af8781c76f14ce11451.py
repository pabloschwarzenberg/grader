#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma

n = int(input("Ingrese un número N: "))

resultado = suma_numeros_naturales(n)

print("La suma de los primeros", n, "números naturales es:", resultado)
      