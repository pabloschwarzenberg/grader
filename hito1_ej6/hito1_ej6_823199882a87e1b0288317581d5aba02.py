def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordenar la lista de números de menor a mayor
    numeros_ord = ', '.join(str(num) for num in numeros)  # Convertir los números a cadena y unirlos con comas
    print(numeros_ord)

# Pedir al usuario que ingrese los números
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

# Llamar a la función para ordenar e imprimir los números
ordenar_numeros(numero1, numero2, numero3)