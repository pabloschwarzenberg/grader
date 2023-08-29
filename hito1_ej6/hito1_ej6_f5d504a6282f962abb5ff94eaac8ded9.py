#Ordenar tres números
def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()  # Ordenar la lista de números de menor a mayor
    numeros_ordenados = ", ".join(map(str, numeros))  # Convertir los números ordenados en una cadena separada por comas
    return numeros_ordenados

# Solicitar al usuario que ingrese los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar los números
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

# Imprimir los números ordenados
print("Números ordenados de menor a mayor: " + numeros_ordenados)
