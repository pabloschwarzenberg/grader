def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

# Solicitar al usuario los tres números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

# Ordenar los números de menor a mayor
numeros_ordenados = ordenar_numeros(num1, num2, num3)

# Imprimir los números ordenados separados por comas
print("Los números ordenados de menor a mayor son:", ", ".join(str(num) for num in numeros_ordenados))
