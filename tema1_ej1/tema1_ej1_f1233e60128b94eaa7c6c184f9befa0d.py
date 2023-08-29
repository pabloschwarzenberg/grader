#Suma de los N primeros números
def suma_primeros_numeros(n):
    suma = (n * (n + 1)) // 2
    return suma



numero_N = int(input("Ingrese el valor de N: "))


resultado = suma_primeros_numeros(numero_N)


print("La suma de los primeros", numero_N, "números naturales es:", resultado)
      