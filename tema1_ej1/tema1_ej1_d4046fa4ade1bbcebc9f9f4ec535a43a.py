#Suma de los N primeros números
def suma_naturales(N):
    suma = N * (N + 1) // 2
    return suma

numero = int(input("Ingrese un número: "))
resultado = suma_naturales(numero)
print("La suma de los primeros", numero, "números naturales es:", resultado)
      