# Función para ordenar los números de menor a mayor
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordenar la lista de números
    return numeros

# Obtener los números del usuario
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
num3 = int(input("Ingresa el tercer número entero: "))

# Llamar a la función para ordenar los números
numeros_ordenados = ordenar_numeros(num1, num2, num3)

# Imprimir los números ordenados separados por coma
print("Números ordenados de menor a mayor:", end=" ")
for i in range(len(numeros_ordenados)):
    if i < len(numeros_ordenados) - 1:
        print(numeros_ordenados[i], end=", ")
    else:
        print(numeros_ordenados[i])
