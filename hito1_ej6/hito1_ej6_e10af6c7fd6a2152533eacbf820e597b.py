# Solicitar tres números enteros al usuario
numeros = []
for i in range(3):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

# Ordenar los números de menor a mayor
numeros.sort()

# Imprimir los números ordenados separados por comas
resultado = ", ".join(str(num) for num in numeros)
print("Números ordenados: " + resultado)