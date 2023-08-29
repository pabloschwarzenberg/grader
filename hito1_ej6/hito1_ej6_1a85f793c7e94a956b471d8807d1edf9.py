#Ordenar tres números
# Pedir al usuario que ingrese tres números enteros
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Crear una lista con los números ingresados
numeros = [numero1, numero2, numero3]

# Ordenar la lista de menor a mayor
numeros.sort()

# Imprimir los números ordenados separados por comas
print("Los números ordenados de menor a mayor son:", ", ".join(map(str, numeros)))
      