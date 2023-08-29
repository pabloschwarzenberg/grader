#Oprograma que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.
def pedir_numeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    return num1, num2, num3

def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

def imprimir_numeros_ordenados(numeros):
    numeros_ordenados = ', '.join(str(numero) for numero in numeros)
    print("Números ordenados de menor a mayor:", numeros_ordenados)

# Pedir al usuario que ingrese los números
numero1, numero2, numero3 = pedir_numeros()

# Llamar a la función para ordenar los números
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

# Imprimir los números ordenados
imprimir_numeros_ordenados(numeros_ordenados)

      