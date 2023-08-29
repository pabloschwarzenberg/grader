def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordena los números de menor a mayor

    # Convierte los números ordenados a una cadena separada por comas
    numeros_ordenados = ', '.join(map(str, numeros))

    return numeros_ordenados


# Solicitar al usuario los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar los números e imprimir el resultado
resultado = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados: ", resultado)
