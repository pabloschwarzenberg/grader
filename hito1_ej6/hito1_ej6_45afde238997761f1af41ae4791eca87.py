# Solicitar al usuario ingresar tres números enteros
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Ordenar los números de menor a mayor
numeros_ordenados = sorted([numero1, numero2, numero3])

# Imprimir los números ordenados separados por comas
resultado = ", ".join(str(num) for num in numeros_ordenados)
print("Números ordenados de menor a mayor:", resultado)

