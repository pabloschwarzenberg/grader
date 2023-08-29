def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    numeros_ordenados = ', '.join(str(num) for num in numeros)
    return numeros_ordenados

# Pedir al usuario que ingrese los números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

numeros_ordenados = ordenar_numeros(num1, num2, num3)

# Imprimir los números ordenados
print("Números ordenados:", numeros_ordenados)
