#Ordenar tres números
# Solicitar los números al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Ordenar los números de menor a mayor
numeros_ordenados = sorted([num1, num2, num3])

# Imprimir los números ordenados separados por comas
resultado = ', '.join(str(num) for num in numeros_ordenados)
print("Los números ordenados de menor a mayor son:", resultado) 