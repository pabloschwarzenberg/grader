#Suma de los N primeros números
def natural_num(n):
    suma = (n *(n + 1)) // 2
    return suma
N = int(input("INgrese el número natural: "))

res = natural_num(N)

print("La suma de los primeros", N, "números naturales es: ", res)

