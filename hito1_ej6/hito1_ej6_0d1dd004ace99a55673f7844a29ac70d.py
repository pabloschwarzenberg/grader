def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)
resultado = ', '.join(map(str, numeros_ordenados))

print("Números ordenados de menor a mayor:", resultado)
