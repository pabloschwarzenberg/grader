def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

# Solicitar tres números al usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Ordenar los números ingresados
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

# Imprimir los números ordenados separados por comas
print("Los números ordenados de menor a mayor son:", ", ".join(map(str, numeros_ordenados)))