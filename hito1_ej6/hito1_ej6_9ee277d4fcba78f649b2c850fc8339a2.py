def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()  # Ordena la lista de números de menor a mayor
    numeros_str = [str(num) for num in numeros]  # Convierte los números a cadenas de texto
    numeros_ordenados = ", ".join(numeros_str)  # Une los números con comas
    return numeros_ordenados

# Solicitar al usuario que ingrese los tres números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

# Ordenar los números e imprimir el resultado
resultado = ordenar_numeros(num1, num2, num3)
print("Los números ordenados son:", resultado)
