#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    numeros_ordenados = ", ".join(str(num) for num in numeros)
    return numeros_ordenados

# Solicitar los números al usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Llamar a la función para ordenar los números
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

# Imprimir los números ordenados
print("Números ordenados de menor a mayor: " + numeros_ordenados)