# Función para ordenar los números
def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    return numeros

# Obtener los números del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamar a la función y obtener los números ordenados
numeros_ordenados = ordenar_numeros(num1, num2, num3)

# Imprimir los números ordenados
print("Los números ordenados de menor a mayor son:", end=" ")
for i in range(len(numeros_ordenados)):
    if i != len(numeros_ordenados) - 1:
        print(numeros_ordenados[i], end=", ")
    else:
        print(numeros_ordenados[i])

