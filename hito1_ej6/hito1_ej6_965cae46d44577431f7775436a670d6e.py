#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordena la lista de números de menor a mayor
    numeros_ordenados = ', '.join(str(num) for num in numeros)
    return numeros_ordenados

# Solicitar al usuario ingresar los tres números enteros
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Llamar a la función y mostrar los números ordenados
numeros_ordenados = ordenar_numeros(num1, num2, num3)
print("Números ordenados: " + numeros_ordenados)
