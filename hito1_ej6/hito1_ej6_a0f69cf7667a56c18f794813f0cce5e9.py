# Pedir al usuario que ingrese tres números enteros
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

# Ordenar los números de menor a mayor
numeros_ordenados = sorted([numero1, numero2, numero3])

# Imprimir los números ordenados separados por comas
resultado = ', '.join(map(str, numeros_ordenados))
print("Los números ordenados son:", resultado)