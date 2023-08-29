#Ordenar tres números
# Función para ordenar los números de menor a mayor
def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()  # Ordena la lista de números
    return numeros

# Pedir al usuario que ingrese los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar los números
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

# Imprimir los números ordenados separados por comas
print("Números ordenados: " + ", ".join(map(str, numeros_ordenados)))
   