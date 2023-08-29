#Ordenar tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Ordenar los números de menor a mayor
numeros_ordenados = sorted([num1, num2, num3])

# Imprimir los números ordenados separados por coma
resultado = ", ".join(map(str, numeros_ordenados))
print("Números ordenados:", resultado)



