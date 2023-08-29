#Ordenar tres números
 # Función para ordenar los números de menor a mayor
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordenar la lista de números de menor a mayor
    return numeros

# Obtener los números del usuario
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

# Llamar a la función para ordenar los números
numeros_ordenados = ordenar_numeros(num1, num2, num3)

# Imprimir los números ordenados separados por comas
print("Números ordenados:", ", ".join(str(num) for num in numeros_ordenados))


      