def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    numeros_ordenados = ', '.join(str(num) for num in numeros)
    return numeros_ordenados


numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

resultado = ordenar_numeros(numero1, numero2, numero3)


print("Números ordenados:", resultado)
