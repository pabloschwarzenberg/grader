#Suma de los N primeros números
   
def sumar (n):
    return (n * (n + 1)) / 2

N = int(input("introduzca N: "))

sumar = sumar (N)

print("resultado", sumar)