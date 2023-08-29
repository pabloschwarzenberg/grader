def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    numeros_ordenados = ', '.join(str(num) for num in numeros)
    print(numeros_ordenados)

# Solicitamos al usuario ingresar los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamamos a la función para ordenar e imprimir los números
ordenar_numeros(num1, num2, num3)
