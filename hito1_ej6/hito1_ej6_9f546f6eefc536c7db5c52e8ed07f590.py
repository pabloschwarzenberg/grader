def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

numeros_ordenados = ordenar_numeros(num1, num2, num3)
resultado = ", ".join(str(numero) for numero in numeros_ordenados)
print("Números ordenados:", resultado)