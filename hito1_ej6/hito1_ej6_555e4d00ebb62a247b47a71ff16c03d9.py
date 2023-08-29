#Ordenar tres número
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Ordenar los números de menor a mayor
numeros = [numero1, numero2, numero3]
numeros.sort()

# Imprimir los números ordenados separados por coma
numeros_ordenados = ", ".join(str(num) for num in numeros)
print("Los números ordenados de menor a mayor son:", numeros_ordenados)