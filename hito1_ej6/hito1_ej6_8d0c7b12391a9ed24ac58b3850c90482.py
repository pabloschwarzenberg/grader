#Ordenar tres números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Encontrar el número más pequeño
minimo = min(num1, num2, num3)

# Encontrar el número más grande
maximo = max(num1, num2, num3)

# Encontrar el número del medio
medio = (num1 + num2 + num3) - minimo - maximo

# Imprimir los números ordenados
print(minimo, medio, maximo, sep=", ")

      