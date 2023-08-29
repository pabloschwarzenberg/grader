# Solicitar al usuario ingresar los tres números enteros
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Ordenar los números utilizando una lista y el método sort()
numeros = [num1, num2, num3]
numeros.sort()

# Imprimir los números ordenados
resultado = ', '.join(map(str, numeros))
print(resultado)
