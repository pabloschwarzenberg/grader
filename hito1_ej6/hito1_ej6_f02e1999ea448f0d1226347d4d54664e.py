def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordenar la lista de números de menor a mayor
    numeros_ordenados = ', '.join(str(num) for num in numeros)  # Convertir los números a cadenas y unirlos con comas
    return numeros_ordenados

# Pedir al usuario que ingrese los números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Llamar a la función para ordenar los números e imprimir el resultado
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados de menor a mayor: " + numeros_ordenados)
