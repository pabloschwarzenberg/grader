#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordenar la lista de números de menor a mayor
    numeros_ordenados = ', '.join(str(num) for num in numeros)
    print("Números ordenados de menor a mayor:", numeros_ordenados)

# Obtener los números del usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Llamar a la función para ordenar e imprimir los números
ordenar_numeros(numero1, numero2, numero3)
     