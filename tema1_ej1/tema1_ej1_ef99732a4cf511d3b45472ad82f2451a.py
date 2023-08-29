def suma_n(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

num = int(input("Ingrese un número n: "))

resultado = suma_n(num)
print("La suma de los primeros", num, "números naturales es:", resultado)