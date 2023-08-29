#Ordenar tres números

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Ordenamos los numero de menor a mayor
numeros_ordenados = sorted([numero1, numero2, numero3])

# Imprimir los números ordenados separados por comas
print("Números ordenados de menor a mayor:", ",".join(map(str, numeros_ordenados)))
      