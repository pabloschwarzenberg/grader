#Ordenar tres números
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

# Utilizar la función sorted para ordenar los números de menor a mayor
numeros_ordenados = sorted([num1, num2, num3])

# Utilizar la función join para unir los números ordenados con comas
resultado = ', '.join(map(str, numeros_ordenados))

print("Números ordenados:", resultado)
     