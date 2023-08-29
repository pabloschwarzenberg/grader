def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordenar la lista de números de menor a mayor
    numeros_str = [str(num) for num in numeros]  # Convertir los números a cadenas de texto
    numeros_ordenados = ", ".join(numeros_str)  # Unir los números con comas

    return numeros_ordenados

# Pedir al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar los números y mostrar el resultado
resultado = ordenar_numeros(num1, num2, num3)
print("Números ordenados:", resultado)
