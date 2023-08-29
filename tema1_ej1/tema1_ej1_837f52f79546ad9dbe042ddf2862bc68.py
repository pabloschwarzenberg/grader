#Suma de los N primeros números
def sumanaturales(n):
    return n * (n + 1) // 2

N = int(input("Ingrece un número: "))
print("La suma de los primeros", N, "números naturales es", sumanaturales(N))      