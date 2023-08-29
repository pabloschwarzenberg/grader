#Ordenar tres números
# Pedir al usuario que ingrese los números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Ordenar los números de menor a mayor
numeros = [num1, num2, num3]
numeros.sort()

# Imprimir los números ordenados
resultado = ', '.join(map(str, numeros))
print("Números ordenados de menor a mayor:", resultado)
