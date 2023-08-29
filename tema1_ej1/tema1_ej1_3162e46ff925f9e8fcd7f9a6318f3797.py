#Suma de los N primeros números
N = int(input("Ingrese un número natural:"))
while (N <= 0):
    N = int(input("Por favor ingrese un número natural:"))
resultado = N * (N+1) / 2
print(resultado)
