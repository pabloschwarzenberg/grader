#Ordenar tres números
def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    numeros_ordenados = ', '.join(str(num) for num in numeros)
    return numeros_ordenados

# Solicitar al usuario ingresar los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar los números
numeros_ordenados = ordenar_numeros(num1, num2, num3)

# Imprimir los números ordenados
print("Números ordenados de menor a mayor: " + numeros_ordenados) 