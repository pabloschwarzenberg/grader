# Solicitar tres números enteros al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Ordenar los números de menor a mayor
numeros_ordenados = sorted([num1, num2, num3])

# Crear una cadena con los números ordenados separados por coma
resultado = ",".join(str(num) for num in numeros_ordenados)

# Imprimir los números ordenados separados por coma
print("Números ordenados:", resultado)
