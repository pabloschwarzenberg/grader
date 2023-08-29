def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordena la lista de números de menor a mayor
    numeros_str = [str(num) for num in numeros]  # Convierte los números a cadenas de texto
    resultado = ", ".join(numeros_str)  # Une los números con comas
    return resultado

# Solicitar los números al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función e imprimir el resultado
resultado = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados:", resultado)