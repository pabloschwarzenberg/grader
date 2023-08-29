#Suma de los N primeros números
N = int(input("Ingrese número: "))
 
resultado = N * (N+1)/2

resultado = 0

for i in range(1,N+1):
    resultado += i

resultado = sum(range(1, N + 1))
print("La suma de los N numeros es -->",resultado)
