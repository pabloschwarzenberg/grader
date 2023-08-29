# Pedir al usuario que ingrese un número N
N = int(input("Ingrese un número N: "))

# Calcular la suma de los N primeros números naturales
suma = 0
for i in range(1, N+1):
    suma += i

# Imprimir el resultado
print(f"La suma de los {N} primeros números naturales es: {suma}")