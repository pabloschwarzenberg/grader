#Ordenar tres números

# Solicitar los números al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Encontrar el número más pequeño
minimo = min(numero1, numero2, numero3)

# Encontrar el número más grande
maximo = max(numero1, numero2, numero3)

# Calcular el número intermedio
intermedio = numero1 + numero2 + numero3 - minimo - maximo

# Mostrar los números ordenados
print("Números ordenados de menor a mayor:", minimo, ",", intermedio, ",", maximo)
