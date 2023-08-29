#Suma de los N primeros números
def sumar(n):
    return (n * (n+1)) / 2

N = int(input("Introduzca N: "))
suma = sumar(N)
print("Resultado: ", suma)