def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordena la lista de números de menor a mayor
    numeros_ordenados = ', '.join(map(str, numeros))  # Convierte los números a cadenas y los une con comas
    print(numeros_ordenados)

# Ejemplo de uso
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

ordenar_numeros(num1, num2, num3)
