def ordenar_numeros(num1, num2, num3):
    numeros = sorted([num1, num2, num3])
    numeros_ordenados = ', '.join(str(num) for num in numeros)
    return numeros_ordenados

# Solicitar tres números al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función y mostrar el resultado
resultado = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados de menor a mayor: " + resultado)