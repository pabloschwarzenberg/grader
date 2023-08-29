def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    numeros_ord = ", ".join(map(str, numeros))
    return numeros_ord

# Solicitar los tres números al usuario
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

# Llamar a la función para ordenar los números
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

# Imprimir los números ordenados
print("Números ordenados de menor a mayor:", numeros_ordenados)