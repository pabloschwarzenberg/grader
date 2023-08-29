numeros = []

# Solicitar al usuario ingresar los números
for i in range(3):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

# Ordenar los números de menor a mayor
numeros.sort()

# Imprimir los números ordenados separados por comas
resultado = ", ".join(str(numero) for numero in numeros)
print("Números ordenados:", resultado)