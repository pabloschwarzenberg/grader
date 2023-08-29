def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

# Solicitar números al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Ordenar los números de mayor a menor
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

# Imprimir los números ordenados separados por comas
resultado = ",".join(str(num) for num in numeros_ordenados)
print("Resultado:", resultado)
