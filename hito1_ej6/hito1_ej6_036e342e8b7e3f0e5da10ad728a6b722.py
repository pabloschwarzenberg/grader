def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordenar los números de menor a mayor
    numeros_ordenados = ", ".join(map(str, numeros))  # Convertir los números a cadena y unirlos con comas
    return numeros_ordenados

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

resultado = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados:", resultado)