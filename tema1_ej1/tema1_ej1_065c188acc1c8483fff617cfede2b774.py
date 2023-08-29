def suma_naturales(n):
    suma = n * (n + 1) / 2
    return suma

n = int(input("Ingrese un numero: "))
 
resultado = suma_naturales(n)
print("La suma de los primeros", n, "numeros naturales es:", resultado)