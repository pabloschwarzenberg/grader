#Suma de los N primeros números
n = int(input("Ingrese un numero --> "))

resultado = n * (n + 1)/2

resultado = 0
for i in range(1, n + 1):
    resultado += i

resultado = sum(range(1, n + 1))
print("La suma de los n numeros es -->",resultado)