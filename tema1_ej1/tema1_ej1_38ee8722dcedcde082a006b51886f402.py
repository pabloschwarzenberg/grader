#Suma de los N primeros números
def sumanumeros(n):
    suma = n * (n + 1) // 2
    return suma

N = int(input("Ingrese un número N: "))
print("La suma de los primeros", N, "números naturales es:", sumanumeros(N))
