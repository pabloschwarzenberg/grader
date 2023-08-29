#Ordenar tres números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Ordenamos los números de menor a mayor usando la función sorted
numeros_ordenados = sorted([num1, num2, num3])

# Imprimimos los números ordenados separados por comas
print(f"{numeros_ordenados[0]}, {numeros_ordenados[1]}, {numeros_ordenados[2]}")