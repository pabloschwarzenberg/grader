# Solicitar los números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Ordenar los números de menor a mayor
numeros = [num1, num2, num3]
numeros.sort()

# Imprimir los números ordenados separados por comas
print(", ".join(str(num) for num in numeros))