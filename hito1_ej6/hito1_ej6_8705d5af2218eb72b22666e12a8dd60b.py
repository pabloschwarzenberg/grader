# Recibir tres números enteros del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

numeros = [num1, num2, num3]
numeros.sort()


resultado = ", ".join(str(num) for num in numeros)
print("Números ordenados de menor a mayor:", resultado)