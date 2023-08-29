def suma_n_numeros(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

# Ejemplo de uso
n = int(input("Ingrese el valor de N: "))
resultado = suma_n_numeros(n)
print("La suma de los primeros", n, "números naturales es:", resultado)
